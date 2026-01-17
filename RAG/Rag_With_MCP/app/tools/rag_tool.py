from app.core.vectorstore import build_vectorstore
from app.core.llm import load_llm

vectorstore=build_vectorstore()
llm=load_llm()

def rag_insurance(question:str)->str:
    """ MCP Tool: RAG Insurance QA """
    docs=vectorstore.similarity_search(question,k=2)
    context="\n".join([d.page_content for d in docs])
    prompt = f"""
              You are a professional insurance assistant.

              Using ONLY the information from the context,
              rewrite the answer as a complete, clear, user-friendly sentence.

              Do NOT add new facts.
              Do NOT answer with keywords or fragments.

              Context:
              {context}

              Question:
              {question}

              Answer (one full sentence):
              """
    return llm(prompt)[0]["generated_text"].strip()


