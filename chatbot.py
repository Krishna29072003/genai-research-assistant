from dotenv import load_dotenv
from langchain_core.messages import SystemMessage , HumanMessage , AIMessage
from langchain_groq import ChatGroq
load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)
chat_history=[SystemMessage(content="You are helpful Agentic AI assistant")]


while True:
    user_input=input('You')
    if user_input=="exit":
        break
    chat_history.append(HumanMessage(content=user_input))
    result=llm.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI:",result.content)

print(chat_history)

