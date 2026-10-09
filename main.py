
from graph import graph
from state import ResearchState

initial_state: ResearchState = {
    "query": "The impact of AI on education in Nigeria",
    "plan": [],
    "findings": [],
    "report": "",
    "approved": False,
}

result = graph.invoke(initial_state)

print("\n--- RESEARCH PLAN ---")
print(result["plan"])

print("\n--- RESEARCH FINDINGS ---")
print(result["findings"])

print("\n--- FINAL REPORT ---")
print(result["report"])