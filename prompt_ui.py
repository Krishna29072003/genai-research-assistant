#imported all the necessary libraries 
import os
from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq
import streamlit as st

#Used Groq API 
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)


#Used Streamlit for Frontend
st.header('Research Tool')


topic=st.text_input("Enter your Prompt")

#Dropdown Inputs
domain = st.selectbox(
    "Research Domain",
    [
        "Artificial Intelligence",
        "Machine Learning",
        "Data Science",
        "Computer Vision",
        "Natural Language Processing",
        "Cyber Security"
    ]
)

section = st.selectbox(
    "Paper Section",
    [
        "Abstract",
        "Introduction",
        "Literature Review",
        "Methodology",
        "Results & Discussion",
        "Conclusion",
        "Future Work"
    ]
)

writing_style = st.selectbox(
    "Writing Style",
    [
        "Formal Academic",
        "Concise",
        "Detailed Technical"
    ]
)

year_range = st.selectbox(
    "Reference Year Range",
    [
        "Last 5 years",
        "Last 10 years",
        "No restriction"
    ]
)

citation_style = st.selectbox(
    "Citation Style",
    [
        "APA",
        "IEEE",
        "MLA"
    ]
)

#prompt template this will tell the referneces for dropdown inputs 

from langchain_core.prompts import PromptTemplate , load_prompt

research_template=load_prompt('template.json')

prompt = research_template.format(
    domain=domain,
    topic=topic,
    section=section,
    style=writing_style,
    year_range=year_range,
    citation_style=citation_style
)


#input_variables=['domain','section','writing_style','year_range','citation_style']

if st.button('Summarize'):
    #st.write("hello")
    result=llm.invoke(prompt)
    st.write(result.content)


'''if st.button('Summarize'):
    chain= research_template| llm
    result=chain.invoke(prompt)
    st.write(result.content)'''