import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel

import uvicorn

from rag_graph import graph
from ingest import ingest_docs


app = FastAPI(
    title="Self-RAG API",
    description="LangGraph + Gemini + ChromaDB + Web Search",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Query(BaseModel):

    question: str


@app.on_event("startup")
def startup_event():

    # Delete old vector database

    if os.path.exists("./chroma_db"):

        print("OLD VECTOR DB DELETED")

    print("STARTING INGESTION...")

    ingest_docs()

    print("INGESTION COMPLETE")

@app.get("/")
def home():

    return {
        "message": "Self-RAG FastAPI Server Running"
    }


@app.post("/chat")
async def chat(query: Query):

    try:

        print(f"\nQUESTION: {query.question}")

        result = graph.invoke(
            {
                "question": query.question,

                "docs": [],

                "relevant_docs": [],

                "context": "",

                "answer": "",

                "web_query": "",
            }
        )

        print("\nANSWER GENERATED")

        return {
            "question": query.question,

            "answer": result.get(
                "answer",
                "No answer generated."
            ),

            "web_query": result.get(
                "web_query",
                None
            ),
        }

    except Exception as e:

        print(f"\nERROR: {e}")

        return {
            "answer": "Internal Server Error. Check backend logs."
        }


if __name__ == "__main__":

    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )