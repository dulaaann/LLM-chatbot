import streamlit as st
from PyPDF2 import PdfReader 
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
import json

with open("env.json") as f:
    env = json.load(f)

API_KEY = env["OPEN_AI_API_KEY"]

#upload pdf files
st.header("Dulan's chatbot")

with st.sidebar:
    st.title("Your Documents")
    file = st.file_uploader("Upload the files and start asking questions", type="pdf")

#Extract the text
if file is not None:
    pdf_reader = PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text+= page.extract_text()


#Break it into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        separators="\n",
        chunk_size=1000,
        chunk_overlap=150,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    
#Generating embaddings
    embaddings = OpenAIEmbeddings(openai_api_key = API_KEY)

#Creating vector store
    vector_store = FAISS.from_texts(chunks,embaddings)

#Get user question
    user_question = st.text_input("Type the question")
#do similarity search
    if user_question : 
        vector_store.similarity_search(user_question)
#output
