from langchain_community.vectorstores import FAISS


def create_vectorstore(chunks, embeddings):

    vectorstore = FAISS.from_documents(
        chunks,
        embeddings
    )

    vectorstore.save_local("vectorstore")

    return vectorstore


def load_vectorstore(embeddings):

    return FAISS.load_local(
        "vectorstore",
        embeddings,
        allow_dangerous_deserialization=True
    )