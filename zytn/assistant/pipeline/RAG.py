from langchain_openai import OpenAIEmbeddings
from langsmith import traceable
from .chain import rag_stuff_chain
from langchain_pinecone import PineconeVectorStore
import os

pinecone_api_key = '34e66b6f-03f5-420d-95e5-a4fa9560977b'
index_name = "e-book"
embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
pinecone = PineconeVectorStore(index_name=index_name, embedding=embeddings, pinecone_api_key=pinecone_api_key)   

chat_history = {}

class RAG:
    """
    RAG class for setting up the RAG pipeline
    """
    def __init__(self):
        self.embedding_function = OpenAIEmbeddings(model="text-embedding-3-large")
        self.retriever = pinecone.as_retriever()

    @traceable(name='RAG Pipeline')
    def get_response(self, query):
        """
        Invokes the RAG chain for response
        """
        retrived_docs = self.retriever.invoke(query)
        result = rag_stuff_chain(query, retrived_docs, chat_history)

        # token_usage['input_tokens'] = token_usage['input_tokens'] + result.usage.prompt_tokens
        # token_usage['output_tokens'] = token_usage['output_tokens'] + result.usage.completion_tokens
        # token_usage['total_tokens'] = token_usage['input_tokens'] + token_usage['output_tokens']

        answer = result.choices[0].message.content
        return answer 
        

