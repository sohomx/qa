from fastapi import FastAPI, Form, Request, Response, File, Depends, HTTPException, status
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.encoders import jsonable_encoder
from langchain.chat_models import ChatOpenAI
from langchain.chains import QAGenerationChain, RetrievalQA
from langchain.chains.summarize import load_summarize_chain
from langchain.text_splitter import TokenTextSplitter
from langchain.document_loaders import PyPDFLoader
from langchain.docstore.document import Document
from langchain.prompts import PromptTemplate
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
import os
import json
import time
import uvicorn
import aiofiles
import csv
from PyPDF2 import PdfReader

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

os.environ["OPENAI_API_KEY"] = ""

def count_pdf_pages(pdf_path):
    try:
        pdf = PdfReader(pdf_path)
        return len(pdf.pages)
    except Exception as e:
        print("Error:", e)
        return None
    
def file_processing(file_path):
    loader = PyPDFLoader(file_path)
    data = loader.load()

    question_gen = ''

    for page in data:
        question_gen += page.page_content

    splitter_gues_gen = TokenTextSplitter(
        model = "gpt-3,5-turbo" , 
        chunk_size = 10000,
        chunk_overlap = 200
    )

    chunks_ques_gen = splitter_gues_gen.split_text(question_gen)

    document_ques_gen = [Document(page_content=t) for t in chunks_ques_gen]

    splitter_ans_gen = TokenTextSplitter(
        model = "gpt-3.5-turbo",
        chunk_size = 10000,
        chunk_overlap = 200
    )

    document_answer_gen = splitter_ans_gen.split_text(
        document_ques_gen
    )

    return document_ques_gen, document_answer_gen

def llm_pipeline(file_path):

    document_ques_gen, document_answer_gen = file_processing(file_path)

    llm_ques_gen_pipeline = ChatOpenAI(
        temperature = 0.3,
        model = "gpt-3.5-turbo"
    )

    prompt_template = """"
    You are an expert at creating questions based on study materials and reference guides.
    Your goal is to prepare a student or teacher for their exam and tests.
    You do this by asking questions about the text below:
    -----------------
    {text}
    -----------------
    Create questions that will prepare the student or teacher for their tests.
    Make sure not to lose any important information.
    QUESTIONS:  
    """

    PROMPT_QUESTIONS = PromptTemplate(
        template = prompt_template,
        input_variables = ["text"]
    )

    refine_template = ("""
    You are an expert at creating practice questions based on study materials and reference guides.
    Your goal is to help a student or teacher for their exams and tests.
    We have received some practice questions to a certain extent: {existing_answer}.
    We have the option to refine the existing questions or add new ones.
    (only if necessary) with some more context below.
    -----------------
    {text}
    -----------------
    Gievn the new context, refine the original questions in English.
    If the context is not helpful, please provide the original questions.
    QUESTIONS:
    """
    )

    REFINE_PROMPT_QUESTIONS = PromptTemplate(
        input_variables = ["existing_answer", "text"],
        template = refine_template
    )

    ques_gen_chain = load_summarize_chain(
        llm = llm_ques_gen_pipeline,
        chain_type= "refine",
        verbose = True,
        question_prompt =  PROMPT_QUESTIONS,
        refine_prompt = REFINE_PROMPT_QUESTIONS

    )
    ques = ques_gen_chain.run(document_answer_gen)

    embeddings = OpenAIEmbeddings()

    vector_store = FAISS.from_documents(document_answer_gen, embeddings)

    llm_answer_gen = ChatOpenAI(
        temperature = 0.1,
        model = "gpt-3.5-turbo"
    )

    ques_list = ques.split("\n")

    ques_list = ques.split("\n")
    filtered_ques_list = [element for element in ques_list if element.endswith('?') or element.endswith('.')]

    answer_generation_chain = RetrievalQA.from_chain_type(
        llm=llm_answer_gen, 
        chain_type="stuff", 
        retriever=vector_store.as_retriever())

    return answer_generation_chain, filtered_ques_list