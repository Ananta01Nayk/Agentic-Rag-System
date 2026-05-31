from retriever import get_retriever
from state import State
retriever = get_retriever()

def retrieve(state: State):
    return {"docs": retriever.invoke(state["question"])}