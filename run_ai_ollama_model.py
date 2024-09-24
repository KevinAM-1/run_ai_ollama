import os
import getpass

from langchain.schema import AIMessage, HumanMessage
import gradio as gr

from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

#Das in den Terminal eingeben: %pip install --upgrade --quiet pypdf

from langchain_community.document_loaders import PyPDFLoader #Document loader

from langchain_experimental.text_splitter import SemanticChunker #Text Splitter 

from langchain_huggingface import HuggingFaceEmbeddings #Embedding Model

from langchain_chroma import Chroma #Vectore Store





system_prompt = "You are a helpful assistant that translates {input_language} to {output_language}."

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            system_prompt,
        ),
        ("human", "{input}"),
    ]
)



#PDF Loader
loader = PyPDFLoader(file_path="")
pages = loader.load_and_split()

#Text Splitter
text_splitter = SemanticChunker(HuggingFaceEmbeddings())
documents = text_splitter.split_documents(pages)

#Instantiate Text embedding Model
embedder = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")

#Instantiate Vector Store
vector = Chroma.from_documents(documents,embedder)

#Retriever
retriever = vector.as_retriever()





model = OllamaLLM(model="llama3.1", temperature=0,)

llm = prompt | model

## end TODO: make it work with gradio

def predict(message, history):
    history_langchain_format = []
    for human, ai in history:
        history_langchain_format.append(HumanMessage(content=human))
        history_langchain_format.append(AIMessage(content=ai))
    history_langchain_format.append(HumanMessage(content=message))
    response = llm.invoke(
        {
            "documents": pages,
            "input": history_langchain_format
        }
    )
    print("User Question: {message}")
    print("Model Answer:")
    print(response)
    return response

gr.ChatInterface(predict).launch()
