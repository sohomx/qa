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