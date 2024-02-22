from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain.tools import  StructuredTool
from langchain.agents.format_scratchpad import format_to_openai_functions
from langchain.prompts import ChatPromptTemplate
from langchain.prompts import MessagesPlaceholder
import json

llm = ChatOpenAI(openai_api_key='123', organization="gluon-meson",
openai_api_base='your-api-base-url', model='gpt-4-turbo-preview', temperature=0, streaming=False)

agent_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are helpful assistant, answer me using a friendly tone, and add some emoji in answer"),
    ("user", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad")
])


def calc_expr(expr: str) -> int:
    return eval(expr)


agent_tools=[StructuredTool.from_function(func=calc_expr, name="Calculator", description="Call this to get the result based on the calculation expression string in python")]

agent = create_openai_tools_agent(llm, agent_tools, agent_prompt)
agent_executor = AgentExecutor(agent=agent, tools=agent_tools, verbose=True)

result = agent_executor.invoke({"input":"Take 3 to the fifth power and multiply that by the sum of twelve and three, then square the whole result"})
print(result["output"])
