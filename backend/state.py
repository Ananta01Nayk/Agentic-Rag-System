from typing import List, TypedDict, Literal
from langchain_core.documents import Document

class State(TypedDict):
    question: str
    need_retrieval: bool

    docs: List[Document]
    relevant_docs: List[Document]

    context: str
    answer: str

    # web query (no loop flags)
    web_query: str