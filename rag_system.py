from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA

def build_rag():

    loader = DirectoryLoader("data", glob="*.md")
    documents = loader.load()

 
    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = splitter.split_documents(documents)


    embeddings = HuggingFaceEmbeddings()

   
    vectorstore = FAISS.from_documents(docs, embeddings)

  
    llm = OpenAI()

    
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever()
    )

    return qa