import streamlit as st
from langchain.llms import OpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
import io
import PyPDF2
import docx

def generate_response(uploaded_file, openai_api_key, query_text):
    if uploaded_file is not None:
        try:
            if uploaded_file.type == 'application/pdf':
                pdf_reader = PyPDF2.PdfReader(io.BytesIO(uploaded_file.read()))
                documents = [pdf_reader.pages[i].extract_text() for i in range(len(pdf_reader.pages))]
            elif uploaded_file.type == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
                doc_reader = docx.Document(io.BytesIO(uploaded_file.read()))
                documents = [para.text for para in doc_reader.paragraphs]
            else:
                documents = [uploaded_file.read().decode()]

            text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
            texts = text_splitter.create_documents(documents)

            embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
            db = Chroma.from_documents(texts, embeddings)
            retriever = db.as_retriever()
            qa = RetrievalQA.from_chain_type(
            llm=OpenAI(openai_api_key=openai_api_key),
            chain_type='stuff',
            retriever=retriever
            )
            return qa.run(query_text)

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            return None


st.set_page_config(page_title='🦜🔗 Ask the Doc App')
st.title('🦜🔗 Ask the Doc App')

uploaded_file = st.file_uploader('Upload an article', type=['txt', 'pdf', 'docx'])
query_text = st.text_input('Enter your question:', placeholder='Please provide a short summary.', disabled=not uploaded_file)


result = []  # Define it before the form so it's always available
with st.form('myform', clear_on_submit=True):
    openai_api_key = st.text_input('OpenAI API Key', type='password', disabled=not (uploaded_file and query_text))
    submitted = st.form_submit_button('Submit', disabled=not(uploaded_file and query_text))

if submitted and openai_api_key:
    with st.spinner('Searching for answers...'):
        response = generate_response(uploaded_file, openai_api_key, query_text)
        result.append(response)

if len(result):
    st.info(result[0])
