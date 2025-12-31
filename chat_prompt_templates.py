from langchain_core.prompts import ChatPromptTemplate


Chat_Template=ChatPromptTemplate.from_messages([
    ('system','You are a helpful {domain} expert'),
    ('human','explain me about this {topic}')
])

prompt=Chat_Template.invoke({'domain':'Gen AI','topic':'Langchain'})
print(prompt)