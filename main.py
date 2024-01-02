__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

import streamlit as st
from llama_index import VectorStoreIndex, ServiceContext
from llama_index.llms import Gemini
from llama_index.embeddings import GeminiEmbedding
from llama_index import SimpleDirectoryReader


@st.cache_resource(show_spinner=False)
def load_data():
    with st.spinner(text="Loading and indexing the Documents – hang tight! This should take 1-2 minutes."):

        llm = Gemini(api_key=st.secrets["GOOGLE_GEMINI_AI"])
        emmbed_model = GeminiEmbedding(api_key=st.secrets["GOOGLE_GEMINI_AI"])
        service_context = ServiceContext.from_defaults(llm=llm, embed_model=emmbed_model, system_prompt="First, attempt to provide an answer based on the context And try to give answer in Detail.If the question is irrelevant with respect to the context then, kindly suggest asking it in the 'Contact Us' tab or Mail to 'devsapariya94@gmail.com' (project means the solution on the problem statement)",)
        __import__('pysqlite3')
        import sys
        sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

        import chromadb
        
        from llama_index.vector_stores import ChromaVectorStore
        db = chromadb.PersistentClient(path="./chroma_db")
        chroma_collection = db.get_or_create_collection("quickstart")
        vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
        index = VectorStoreIndex.from_vector_store(
            vector_store,
            service_context=service_context,
        )
        return index

index = load_data()

if "chat_engine" not in st.session_state.keys(): # Initialize the chat engine
    st.session_state.chat_engine = index.as_chat_engine(chat_mode="context", verbose=True)

cl1, cl2, cl3 = st.columns(3)
current = "home"
with cl1:
    if st.button("Home"):
        current = "home"
with cl2:
    if st.button("About us"):
        current = "about"

with cl3:
    if st.button("Contact us"):
        current = "contact"

if current == "home":
    st.write("This side project is just for fun 😊")
    st.title("Chat With the AI of Digital Fortress (About our Project of Smart India Hackathon-2023)")
    st.info("For More information Check out [this](https://www.linkedin.com/posts/imabhisht_working-model-presentation-activity-7136969797811982336-O70V?utm_source=share&utm_medium=member_desktop)", icon="📃")
    st.info("Can You Start with 'tell me about the team' or 'What is the problem Statement'", icon="🤔")
          
    if "messages" not in st.session_state.keys(): 
        st.session_state.messages = [
            {"role": "assistant", "content": "Ask me questions about our Project"}
        ]
    prompt = st.chat_input("Your question")
        
    if prompt:  # Prompt for user input and save to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

    # If the last message is not from the assistant, generate a new response
    if st.session_state.messages and st.session_state.messages[-1]["role"] != "assistant":
        current = "home"
        with st.spinner("Thinking..."):
            response = st.session_state.chat_engine.chat(prompt)
            current = "home"
            st.write(response.response)
            message = {"role": "assistant", "content": response.response}
            st.session_state.messages.append(message)  # Add response to message history

    # Display the prior chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

about_us_content = """
## Project Overview

Welcome to our AI app -of **Digital Fortress**. We Build this Project In Smart India Hackathon 2023 for the problem statement "De-anonymisation for monitoring and tracking of illegal activities performed using cryptocurrency transaction technology" By NTRO (National Technical Research Organisation).

## Team (Digital Fortress)

### Team Leader
- **Abhisht Chouhan**
    - [Linkedin](https://www.linkedin.com/in/imabhisht/)
    - [Github](https://github.com/imabhisht)

### Team Members
1. **Rishit Lunia**
   - [Linkedin](https://www.linkedin.com/in/rishit-lunia-b3a33b226/)
   - [Github](https://github.com/RishitLunia3108)

2. **Dev Sapariya**
   - [Linkedin](https://www.linkedin.com/in/devsapariya94/)
   - [Github](https://github.com/devsapariya94)

3. **Reha Shah**
   - [Linkedin](https://www.linkedin.com/in/reha-shah-476b9124b/)
   - [Github](https://github.com/rehashah9)

4. **Apeksha Shah**
   - [Linkedin](https://www.linkedin.com/in/apeksha-shah-5a560525b/)
   - [Github](https://github.com/ShahApeksha)

5. **Astha Bhatt**
   - [Linkedin](https://www.linkedin.com/in/astha-bhatt-b0957120b/)
   - [Github](https://github.com/AsthaBhatt1210)

Feel free to reach out to us if you have any questions, suggestions, or collaboration opportunities. We're excited about the potential impact of our project and would love to hear from you!

"""

if current == "about":
    st.markdown(about_us_content)

if current == "contact":
    st.title("Contact Us")
    st.write("For any Feedback, Suggestions or Queries, Please feel free to contact us at: devsapariya94@gmail.com")
