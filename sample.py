from llama_index.llms.gemini import Gemini
from llama_index.llms.cohere import Cohere
from llama_index.core.agent import ReActAgent
from llama_index.core.tools import FunctionTool

llm = Cohere(model='command', api_key=API_KEY_C) 
 
def mult(a:float, b:float) -> float:
  return a*b

def add(a:float, b:float) -> float:
  return a+b

def sub(a:float, b:float) -> float:
  return a-b

def div(a:float, b:float) -> float:
  return a//b

add_tool = FunctionTool.from_defaults(fn=add)
sub_tool = FunctionTool.from_defaults(fn=sub)
mult_tool = FunctionTool.from_defaults(fn=mult) 
div_tool = FunctionTool.from_defaults(fn=div)

tools_list = [add_tool, sub_tool, mult_tool, div_tool]\

agent = ReActAgent.from_tools(
    tools_list,
    llm=llm,
    verbose=True
)

response = agent.chat('What is 20-(5+6)? Use the various tools provided to solve the problem')
print(response)
