
from graph import research_graph


def main():
    default_query = "The impact of AI on education in Nigeria"
    query = input("What topic do you want to research? ").strip() or default_query

    initial_state = {
        "query": query,
        "plan": [],
        "findings": [],
        "analysis": "",
        "report": "",
        "approved": False,
    }

    result = research_graph.invoke(initial_state)

    print("\n" + "=" * 50)
    print("RESEARCH PLAN")
    print("=" * 50)

    for question in result["plan"]:
        print(question)

    print("\n" + "=" * 50)
    print("RESEARCH FINDINGS")
    print("=" * 50)

    for finding in result["findings"]:
        print(finding)

    print("\n" + "=" * 50)
    print("RESEARCH ANALYSIS")
    print("=" * 50)

    print(result["analysis"])

    print("\n" + "=" * 50)
    print("FINAL RESEARCH REPORT")
    print("=" * 50)

    print(result["report"])

    print("\nApproved:", result["approved"])


if __name__ == "__main__":
    main()