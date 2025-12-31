from langchain_core.prompts import ChatPromptTemplate ,MessagesPlaceholder

chat_template=ChatPromptTemplate(
    [('system','You are a helpful customer support agent'),
     MessagesPlaceholder(variable_name='chat_History'),
     ('human','{query}')]
)
chat_History=[]

with open('chat_history.txt') as f:
    chat_History.extend(f.readlines())

print(chat_History)

prompt=chat_template.invoke({'chat_History':chat_History,'query':'where is my refund'})
print(prompt)

