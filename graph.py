
from langgraph.graph import StateGraph, START, END
from state import ResearchState

from agents import (
    planner_agent,
    researcher_agent,
    analysis_agent,
    writer_agent,
    reviewer_agent,
)


def route_after_review(state: ResearchState):
    if state["approved"]:
        return "end"

    return "revise"


builder = StateGraph(ResearchState)

builder.add_node("planner", planner_agent)
builder.add_node("researcher", researcher_agent)
builder.add_node("analysis", analysis_agent)
builder.add_node("writer", writer_agent)
builder.add_node("reviewer", reviewer_agent)

builder.add_edge(START, "planner")
builder.add_edge("planner", "researcher")
builder.add_edge("researcher", "analysis")
builder.add_edge("analysis", "writer")
builder.add_edge("writer", "reviewer")

builder.add_conditional_edges(
    "reviewer",
    route_after_review,
    {
        "end": END,
        "revise": "writer",
    },
)

research_graph = builder.compile()