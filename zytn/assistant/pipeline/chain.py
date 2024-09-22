import openai
from langsmith.wrappers import wrap_openai
openai_client = wrap_openai(openai.Client())
from langsmith import traceable
from .prompts import qa_prompt


qa_prompt = qa_prompt()


@traceable(name='Format Docs')
def format_docs(docs):
    """
    Stuffs the documents to a string
    """
    stuffed_docs = {}
    i = 1
    for doc in docs:
        string = {}
        string['content'] = doc.page_content
        string['page number'] = doc.metadata["Page number"]
        stuffed_docs[f'context_document_{i}'] = string
        i=i+1
        
    return str(stuffed_docs)

@traceable(name='RAG Stuff Chain')
def rag_stuff_chain(query, docs, chat_history):
    """
    RAG chain for answering the user query
    """
    doc_string = format_docs(docs)
    prompt = qa_prompt.format(context=doc_string, input=query, chat_history=chat_history)
    messages=[
            {"role": "system", "content": prompt}
        ]
    result = openai_client.chat.completions.create(
        messages=messages,
        model="gpt-3.5-turbo", 
        temperature=0,
        top_p=0.2,
        seed=0
    )
    return result