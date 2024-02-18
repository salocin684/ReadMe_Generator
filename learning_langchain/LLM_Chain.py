from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()
llm = ChatOpenAI(openai_api_key=os.getenv('OPENAI_API_KEY'))

#print(llm.invoke("how can langsmith help with testing?"))²

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are world class technical documentation writer."),
    ("user", "{input}")
])

#chain = prompt | llm 

#print(chain.invoke({"input": "how can langsmith help with testing?"}))

output_parser = StrOutputParser()
chain = prompt | llm | output_parser

print(chain.invoke({"input": "how can langsmith help with testing?"}))
