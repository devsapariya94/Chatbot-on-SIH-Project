
# AI Chat Bot

This chat bot utilizes the knowledge from our **Smart India Hackathon 2023 (SIH)** project documents to provide accurate and informed responses to user questions.


## Experiance 
You can experience it by visiting [this link](https://digital-fortress-ai.streamlit.app/).

## Technical Aspect
- Front End: Developed using Streamlit.
- Indexing and Querying: Employed the llama index.
- Language Model: Utilized Google Gemini AI as the Large Language Model (LLM).

## Run Locally
To run locally, ensure you have Python installed on your machine. Follow these steps:

1. Clone the repository:
```bash
git clone https://github.com/devsapariya94/Chatbot-on-SIH-Project
cd Chatbot-on-SIH-Project
```

2. Install the requirements:
```bash
pip install -r requirements.txt
```

3. Run the project:
```bash
streamlit run main.py
```

### Run With Your own data
1. Create a folder named "data" and add your desired data for the chat bot.
2. Run the following commands:
```bash
python creating_embedding.py
streamlit run main.py
```


## Change About Us Page
To modify the "About Us" page, follow these steps:

1. Open the main.py file in a text editor or integrated development environment (IDE).

2. Locate the section that contains the Markdown (md) code for the "About Us" page. It is typically marked with comments or within a specific function.

3. Edit the Markdown code to reflect the updated content for the "About Us" page. You can use standard Markdown syntax for formatting.

4. Save the changes.

5. If the chat bot is already running locally, you may need to restart it for the changes to take effect. Stop the current execution and ``` run the streamlit run main.py ``` command again.
