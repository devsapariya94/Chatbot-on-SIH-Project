from llama_index.llms import Gemini
from llama_index.embeddings import GeminiEmbedding
from llama_index import VectorStoreIndex, ServiceContext, SimpleDirectoryReader
from llama_index.vector_stores import ChromaVectorStore
from llama_index.storage.storage_context import StorageContext
import os
from dotenv import load_dotenv
import chromadb
load_dotenv()
# Create a Gemini instance
llm = Gemini(api_key=os.getenv("GOOGLE_GEMINI_AI"))
embedding_model = GeminiEmbedding(api_key=os.getenv("GOOGLE_GEMINI_AI"))

service_context = ServiceContext.from_defaults(llm=llm, embed_model=embedding_model, system_prompt="First, attempt to provide an answer based on the context And try to give answer in Detail.If the question is irrelevant with respect to the context then, kindly suggest asking it in the 'Contact Us' tab or Mail to 'devsapariya94@gmail.com' (project means the solution on the problem statement)")
reader = SimpleDirectoryReader(input_dir="./data", recursive=True)
documents = reader.load_data()



db = chromadb.PersistentClient(path="./chroma_db")
chroma_collection = db.get_or_create_collection("quickstart")
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
storage_context = StorageContext.from_defaults(vector_store=vector_store)
index = VectorStoreIndex.from_documents(
    documents, storage_context=storage_context, service_context=service_context
)
