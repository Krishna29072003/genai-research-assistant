from dotenv import load_dotenv
from langchain_core.messages import SystemMessage , HumanMessage , AIMessage
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field
load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)



# String Output Parser
'''template1= PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']

)
template2= PromptTemplate(
    template='Write a 5 line pointer summary on {text}',
    input_variables=['text']
)
parser=StrOutputParser()
Chain= template1 | llm | parser | template2 | llm | parser
result=Chain.invoke({'topic':'Black Hole'})
print(result)'''

#Pydantic Output Parser 

class Person(BaseModel):
    name : str = Field(description="Name of the Person")
    age : int = Field(gt=18,description="age of the person")
    city : str = Field(description="Name of the city the person belongs to ")

template= PromptTemplate(
    template='Write the name , age ,city of a fictional character who belongs to {place}',
    input_variables=['place']
)

parser=PydanticOutputParser(pydantic_object=Person)

chain= template | llm | parser 
result=chain.invoke({'place':'Vrindavan'})
print(result)








