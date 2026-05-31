import os

from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from retriever import get_vectorstore

load_dotenv()

def ingest_docs():

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    pdf_path = os.path.join(BASE_DIR, "data", "Ananta_Nayak_AI_ML_Resume _.pdf")

    print("Loading PDF:", pdf_path)

    loader = PyPDFLoader(pdf_path)

    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(docs)

    get_vectorstore(chunks)

    print("Documents ingested successfully.")