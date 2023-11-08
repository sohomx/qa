# qa
QA generator application where you upload a pdf (chunk of text), creates embeddings and generates open-ended questions and answers

<p align="center">
<!-- <a href=https://github.com/sohomx/qa target="_blank">
<img src='/placeholder.jpg' width="100%" alt="Banner" /> -->
</a>
</p>



<p align="center">
<img src="https://img.shields.io/github/contributors/sohomx/qa" alt="GitHub contributors" />
<img src="https://img.shields.io/github/discussions/sohomx/qa" alt="GitHub discussions" />
<img src="https://img.shields.io/github/issues/sohomx/qa" alt="GitHub issues" />
<img src="https://img.shields.io/github/issues-pr/sohomx/qa" alt="GitHub pull request" />
</p>

<p></p>
<p></p>

## 🔍 Table of Contents

* [💻 Stack](#stack)

* [📝 Project Summary](#project-summary)

* [⚙️ Setting Up](#setting-up)

* [🚀 Run Locally](#run-locally)

* [🙌 Contributors](#contributors)

* [📄 License](#license)

## 💻 Stack

- [fastapi](https://fastapi.tiangolo.com/): A modern, fast (high-performance) web framework for building APIs with Python.
- [uvicorn](https://www.uvicorn.org/): A lightning-fast ASGI server implementation, perfect for running FastAPI applications.
- [jinja2](https://palletsprojects.com/p/jinja/): A full-featured template engine for Python, used for generating dynamic HTML pages.
- [python-multipart](https://github.com/andrew-d/python-multipart): A streaming multipart parser for Python, used for handling file uploads in FastAPI.
- [PyPDF2](https://github.com/mstamy2/PyPDF2): A library for extracting text and metadata from PDF files.
- [langchain](https://github.com/langchain/langchain): A Python library for language detection and translation.
- [openai](https://github.com/openai/openai-python): A Python library for interacting with the OpenAI GPT-3 language model.
- [tiktoken](https://github.com/thoppe/tiktoken): A Python library for counting tokens in a text string, useful for estimating costs in language models.

## 📝 Project Summary

## ⚙️ Setting Up

#### Your Environment Variable

- Step 1

- Step 2

## 🚀 Run Locally
1.Clone the qa repository:
```sh
git clone https://github.com/sohomx/qa
```
2.Install the dependencies with one of the package managers listed below:
```bash
pip install -r requirements.txt
```
3.Start the development mode:
```bash
python app.py
```

## 🙌 Contributors

<table style="border:1px solid #404040;text-align:center;width:100%">
<tr><td style="width:14.29%;border:1px solid #404040;">
        <a href="https://github.com/sohomx" spellcheck="false">
          <img src="https://avatars.githubusercontent.com/u/84140043?v=4?s=100" width="100px;" alt="sohomx"/>
          <br />
          <b>sohomx</b>
        </a>
        <br />
        <a href="https://github.com/sohomx/qa/commits?author=sohomx" title="Contributions" spellcheck="false">
          6 contributions
        </a>
      </td></table>

## 📄 License

[**Add Your License**](https://choosealicense.com)

--------------------------
how it works:

autogenerating questions and answers (in subjective form) by uploading a subtext of pdf

you can upload a single chapter of history or english literature and the app will spit out "x" number of questions and answers as mentioned. for now we have kept in open ended and in the 
v2 version it will have MCQs as well. here is the example of how it works:

here you upload the corpus of text in the form of pdf where you want to generate questions from (mention how many pages of questions you would want):
![image](https://github.com/sohomx/qa/assets/84140043/48d23938-ab76-406d-91ec-d651808ad04f)

and now you would see how it autogenerates both Q and A based on the topics uploaded in the subjective manner:
![image](https://github.com/sohomx/qa/assets/84140043/f78d648c-270a-4874-a15c-b597744b4792)

(you can also store both Q and A in a database if the school wishes it )
![image](https://github.com/sohomx/qa/assets/84140043/e76b2e26-2e49-4f26-92dc-6bb978199be3)



