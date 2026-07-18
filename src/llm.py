from langchain_ollama import ChatOllama


def load_llm():

    llm = ChatOllama(
        model="llama3.2:1b",
        temperature=0
    )

    return llm