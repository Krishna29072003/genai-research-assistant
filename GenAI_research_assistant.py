'''from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
load_dotenv()
Chat_History=[]

chatmodel=ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are a GenAI academic expert.

STRICT RULES:
- Write ONLY the Introduction section
- Limit answer to EXACTLY 5 bullet points
- Do NOT give examples
- Do NOT include references
- Do NOT include bibliography
- Do NOT add headings
- Use formal academic tone
"""
    ),
    MessagesPlaceholder(variable_name="Chat_History"),
    ("human", "Explain {topic}")
])


chain =prompt | chatmodel

while True:
    user_input=input("You")
    if user_input == "exit":
        print("chat ended")
        break

    Chat_History.append(HumanMessage(content=user_input))
    response=chain.invoke({"topic":user_input,"Chat_History":Chat_History})
    Chat_History.append(AIMessage(content=response.content))
    print("AI:",response.content)

import json; json.dump([{"type": m.__class__.__name__, "content": m.content} for m in Chat_History], open("chat_history.json","w"), indent=2)
'''

import json
import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from langchain_groq import ChatGroq

load_dotenv()

# ---- Page config ----
st.set_page_config(page_title="GenAI Research Assistant", page_icon="📘")
st.title("📘 GenAI Research Assistant")

# ---- Session State for Chat History ----
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ---- LLM ----
chatmodel = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

# ---- Prompt ----
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are a GenAI academic expert.

STRICT RULES:
- Write ONLY the Introduction section
- Limit answer to EXACTLY 5 bullet points
- Do NOT give examples
- Do NOT include references
- Do NOT include bibliography
- Do NOT add headings
- Use formal academic tone
"""
    ),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "Explain {topic}")
])

# ---- Chain ----
chain = prompt | chatmodel

# ---- Display existing messages ----
for msg in st.session_state.chat_history:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.write(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.write(msg.content)

# ---- User input ----
user_input = st.chat_input("Ask about a GenAI topic...")

if user_input:
    # Add user message
    st.session_state.chat_history.append(HumanMessage(content=user_input))
    with st.chat_message("user"):
        st.write(user_input)

    # Generate response
    with st.spinner("Thinking..."):
        response = chain.invoke({
            "topic": user_input,
            "chat_history": st.session_state.chat_history
        })

    # Add AI message
    st.session_state.chat_history.append(AIMessage(content=response.content))
    with st.chat_message("assistant"):
        st.write(response.content)

# ---- Save chat history ----
if st.button("💾 Save Chat History"):
    json.dump(
        [
            {"type": m.__class__.__name__, "content": m.content}
            for m in st.session_state.chat_history
        ],
        open("chat_history.json", "w"),
        indent=2
    )
    st.success("Chat history saved to chat_history.json")
