from llama_index.llms import Gemini
from llama_index.embeddings import GeminiEmbedding
from llama_index import VectorStoreIndex, ServiceContext, SimpleDirectoryReader
from llama_index.vector_stores import ChromaVectorStore,DeepLakeVectorStore, MilvusVectorStore
from llama_index.storage.storage_context import StorageContext
import os
from dotenv import load_dotenv
import chromadb
load_dotenv()
# Create a Gemini instance
llm = Gemini(api_key=os.getenv("GOOGLE_GEMINI_AI"))
embedding_model = GeminiEmbedding(api_key=os.getenv("GOOGLE_GEMINI_AI"))

service_context = ServiceContext.from_defaults(llm=llm, embed_model=embedding_model)

reader = SimpleDirectoryReader(input_dir="./data", recursive=True)
documents = reader.load_data()



# db = chromadb.PersistentClient(path="./chroma_db")
# chroma_collection = db.get_or_create_collection("quickstart")
# vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
# storage_context = StorageContext.from_defaults(vector_store=vector_store)
# index = VectorStoreIndex.from_documents(
#     documents, storagecontext=storage_context, service_context=service_context
# )



