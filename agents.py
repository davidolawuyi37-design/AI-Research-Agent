from state import ResearchState
from llm import llm

def planner(state: ResearchState):
    topic = state.get("topic", "")
    prompt = f"""
    Create a research plan for this topic:
    {topic}

    Return 4 specific research questions.
    """

    response = llm.invoke(prompt)

    return {"plan": [response.content]}