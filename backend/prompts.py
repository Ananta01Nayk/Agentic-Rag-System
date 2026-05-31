# prompts.py

from langchain_core.prompts import ChatPromptTemplate

decide_retrieval_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You decide whether retrieval is needed.

            Return JSON:
            {
                "should_retrieve": true/false
            }

            Rules:
            - True if answer requires documents
            - True if answer needs recent/current information
            - False for simple general knowledge
            - If unsure choose True
            """
        ),

        (
            "human",
            "Question: {question}"
        ),
    ]
)

direct_generation_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            Answer the question using only general knowledge.

            Do not assume access to documents.

            If unsure say:
            "I don't know."
            """
        ),

        (
            "human",
            "{question}"
        ),
    ]
)

is_relevant_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            Check if document is relevant.

            Return JSON:
            {
                "is_relevant": true/false
            }
            """
        ),

        (
            "human",
            """
            Question:
            {question}

            Document:
            {document}
            """
        ),
    ]
)

rag_generation_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a RAG assistant.

            Answer ONLY using provided context.

            If answer not found say:
            "No relevant document found."

            Do not hallucinate.
            """
        ),

        (
            "human",
            """
            Question:
            {question}

            Context:
            {context}
            """
        ),
    ]
)

rewrite_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            Rewrite question into a web search query.

            Rules:
            - Keep query short
            - Use keywords only
            - Add recent if needed
            - Do not answer
            """
        ),

        (
            "human",
            "Question: {question}"
        ),
    ]
)