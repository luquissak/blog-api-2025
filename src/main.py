import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from langchain import hub

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import GoogleGenerativeAI
from langserve import add_routes

google_api_key = os.environ["GOOGLE_API_KEY"]

llm = GoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=google_api_key)

system_template = "Você é um tutor de Filosofia, nível acadêmico especializado:"
prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)

bot_chain = (
    prompt_template
    | llm
    | StrOutputParser()
)

app = FastAPI(
  title="LangChain Server",
  version="1.0",
  description="A simple API server using LangChain's Runnable interfaces",
)

add_routes(
    app,
    bot_chain,
    path="/chain",
)

@app.get("/")
def read_root():
    html = ""
    with open("index.html", "r") as f:
        html = f.read()
    return HTMLResponse(content=html, status_code=200)