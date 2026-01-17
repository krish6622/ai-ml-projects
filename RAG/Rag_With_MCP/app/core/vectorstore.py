from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pathlib import Path
from app.core.embeddings import load_embeddings

def build_vectorstore():
    # base_dir=Path(__file__).resolve().parents[2]
    # file_path="";

    loader=TextLoader(r"D:\Codes\AI-ML Projects\ai-ml-projects\RAG\Rag_With_MCP\data\insurance_docs\policy.txt")
    documents=loader.load()

    splitter= RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=50
    )

    docs=splitter.split_documents(documents)

    embeddings=load_embeddings()
    return FAISS.from_documents(docs,embeddings)