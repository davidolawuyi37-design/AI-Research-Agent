from langgraph.graph import StateGraph, START, END
from state import ResearchState
from agents import planner

builder = StateGraph(ResearchState)

builder.add_node("planner", planner)

builder.add_edge(START, "planner")
builder.add_edge("planner", END)

graph = builder.compile()