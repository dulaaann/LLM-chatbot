import streamlit as st
from PyPDF2 import PdfReader 
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain_google_genai import ChatGoogleGenerativeAI
import json

with open("env.json") as f:
    env = json.load(f)

GOOGLE_API_KEY = env["GOOGLE_API_KEY"]

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
    embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    google_api_key=GOOGLE_API_KEY
)


#Creating vector store
    vector_store = FAISS.from_texts(chunks,embeddings)

#Get user question
    user_question = st.text_input("Type the question")
#do similarity search
    if user_question : 
        matches = vector_store.similarity_search(user_question,k=3)
        # for match in matches:
        #     st.write(match.page_content)
        llm = ChatGoogleGenerativeAI(
            model="gemini-2.0-flash-exp",
            google_api_key=GOOGLE_API_KEY,
            temperature=0,
            max_tokens=1000
            )
#output
        chain = load_qa_chain(llm,chain_type="stuff")
        response = chain.run( input_documents = matches, question = user_question)
        st.write(response)