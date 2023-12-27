import streamlit as st

from langchain.llms import HuggingFaceHub

def get_answer(query):
    llm = HuggingFaceHub(repo_id = "google/flan-t5-large")
    return llm(query)

def get_query():
    return st.text_input("You: ", key="input")

st.set_page_config(page_title="My App", page_icon=":shark:")
st.header("My App")

query = get_query()
answer = get_answer(query)

submit = st.button("Submit")
if submit:
    st.subheader("Answer: ")
    st.write(answer)
