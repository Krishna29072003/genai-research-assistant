from langchain_core.messages import SystemMessage , HumanMessage , AIMessage
from dotenv import load_dotenv

from langchain_groq import ChatGroq
load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

messages=[
    SystemMessage(content='You are a helpful Agentic AI assistant'),
    HumanMessage(content='Tell me about langchain')
]

result=llm.invoke(messages)
messages.append(AIMessage(content=result.content))
print(messages)

