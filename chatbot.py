from langchain_google_genai import ChatGoogleGenerativeAI
from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from dotenv import load_dotenv

load_dotenv()

# Model
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.5,
    max_output_tokens=500
)

# State
class AnswerState(TypedDict):
    role: str
    answer: str

# Node
def llm(state: AnswerState) -> AnswerState:
    role = state["role"]
    prompt = f"Give the most required skills for a {role} job role don't provide any explanation for any skill just give skill and some additional bonus skill to addon"
    
    result = model.invoke(prompt)
    
    return {
        "role": role,
        "answer": result.content
    }

# Graph
graph = StateGraph(AnswerState)

graph.add_node("llm", llm)
graph.add_edge(START, "llm")
graph.add_edge("llm", END)

agent = graph.compile()

# Invoke
output = agent.invoke({"role": "Data analyst"})
print(output["answer"])
