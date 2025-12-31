from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from langchain_groq import ChatGroq

load_dotenv()

app = FastAPI()

# ---- LLM ----
llm = ChatGroq(
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

chain = prompt | llm

# ---- Request Schema ----
class ChatRequest(BaseModel):
    topic: str
    history: list[str] = []

# ---- Response Schema ----
class ChatResponse(BaseModel):
    answer: str

# ---- API Endpoint ----
@app.post("/ask", response_model=ChatResponse)
def ask(request: ChatRequest):
    chat_history = []

    for msg in request.history:
        chat_history.append(HumanMessage(content=msg))

    response = chain.invoke({
        "topic": request.topic,
        "chat_history": chat_history
    })

    return {"answer": response.content}
