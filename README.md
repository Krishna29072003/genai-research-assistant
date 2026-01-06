# GenAI Research Assistant

A GenAI-powered research assistant built using LangChain and Groq LLMs.  
The project demonstrates prompt engineering, conversational memory, and two delivery modes:
1. Streamlit-based UI for demos and internal use  
2. FastAPI-based backend for production-style API integration  

---

## Features

- Academic-style response generation
- Strict prompt control (no examples, no references, controlled format)
- Multi-turn conversational memory
- Streamlit chat UI for quick experimentation
- FastAPI backend exposing GenAI logic as REST API
- Swagger UI for easy API testing
- Chat history persistence (JSON)

---

## Tech Stack

- Python
- LangChain
- Groq LLM
- Streamlit
- FastAPI
- Uvicorn
- Hugging Face compatible models
- OpenAI / Gemini compatible structured prompting
- Pydantic


## Structured Output & Model Compatibility

This project demonstrates structured and validated LLM outputs across multiple model providers.

- For models that natively support structured outputs (e.g., OpenAI, Gemini), schema-driven prompting is used to guide responses into predictable formats.
- For models that do not provide native structured output support (e.g., Groq, Hugging Face-hosted models), LangChain output parsers are employed to enforce structure and consistency.
- PydanticOutputParser is used to validate and enforce schemas, ensuring type safety and reliability of LLM responses regardless of the underlying model provider.

This approach enables a unified, provider-agnostic design where GenAI applications can switch between different LLM backends while maintaining consistent and validated outputs.
