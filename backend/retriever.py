import os

from langchain_chroma import Chroma

from langchain_community.embeddings import (
    HuggingFaceEmbeddings
)

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


def get_vectorstore(chunks=None):

    if chunks:

        vectorstore = Chroma.from_documents(
            documents=chunks,
            embedding=embeddings,
            persist_directory="./chroma_db"
        )

        return vectorstore

    return Chroma(
        persist_directory="./chroma_db",
        embedding_function=embeddings
    )


def get_retriever():

    vectorstore = get_vectorstore()

    return vectorstore.as_retriever(
        search_kwargs={"k": 2}
    )