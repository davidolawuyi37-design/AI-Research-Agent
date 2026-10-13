from llm import llm
from state import ResearchState


def _normalize_response(content):
    if isinstance(content, list):
        return "\n".join(str(item) for item in content)
    return str(content)


def planner_agent(state: ResearchState):
    prompt = f"""
You are an AI research planning assistant.

The user wants to research this topic:
{state["query"]}

Create a research plan containing exactly 4 specific
research questions that will help investigate this topic. The questions must be clear, relevant, and logically ordered.

Return only the 4 questions as a numbered list.
"""

    response = llm.invoke(prompt)
    plan_text = _normalize_response(response.content)

    plan = [
        line.strip().lstrip("0123456789. )")
        for line in plan_text.splitlines()
        if line.strip()
    ]

    return {"plan": plan[:4]}


def researcher_agent(state: ResearchState):
    plan = state["plan"]

    prompt = f"""
You are an AI research assistant.

Research topic:
{state["query"]}

Research questions:
{plan}

For each research question:
1. Provide relevant findings.
2. Explain the important facts clearly.
3. Include useful examples and references where appropriate.
4. Do not invent statistics, studies, or sources.
5. If you are uncertain about a fact, say so.

Organize your findings by research question.

Return your findings in a structured format, clearly indicating which findings correspond to each research question. Also return them in a clear numbered list.
"""

    response = llm.invoke(prompt)
    findings_text = _normalize_response(response.content)

    findings = [
        line.strip()
        for line in findings_text.splitlines()
        if line.strip()
    ]

    return {"findings": findings}


def analysis_agent(state: ResearchState):
    prompt = f"""
You are an AI research analysis assistant.

Research topic:
{state["query"]}

Research plan:
{state["plan"]}

Research findings:
{state["findings"]}

Analyze the findings carefully.

You should:
1. Identify the most important findings.
2. Explain the relationships between the findings.
3. Identify any gaps, uncertainties, or contradictions in the research.
4. Separate well-supported information from claims that need further verification.
5. Organize the analysis into clear sections with headings.

Do not invent facts or sources.

Return a clear, structured research analysis report, clearly indicating which findings support each part of the analysis. Also return it in a clear numbered list.
"""

    response = llm.invoke(prompt)
    analysis = _normalize_response(response.content)

    return {"analysis": analysis}


def writer_agent(state: ResearchState):
    prompt = f"""
You are a professional research report writer.

Research topic:
{state["query"]}

Research plan:
{state["plan"]}

Research findings:
{state["findings"]}

Research analysis:
{state["analysis"]}

Write a complete research report based on the information provided.

Use this structure:

1. Title
2. Introduction
3. Research Objectives
4. Main Discussion
5. Key Findings
6. Conclusion
7. Recommendations

Requirements:
- Use clear and formal English.
- Organize the report with meaningful headings.
- Explain the important findings.
- Make recommendations relevant to the findings.
- Do not invent statistics, citations, facts, or sources.
- Clearly acknowledge important uncertainties or gaps in the research.
- Do not claim that the web research was conducted.

Return only the completed research report.
"""

    response = llm.invoke(prompt)
    report = _normalize_response(response.content)

    return {"report": report}


def reviewer_agent(state: ResearchState):
    prompt = f"""
You are a strict research report reviewer.

Research topic:
{state["query"]}

Research plan:
{state["plan"]}

Research findings:
{state["findings"]}

Research analysis:
{state["analysis"]}

Report to review:
{state["report"]}

Review the report for:
1. Relevance to the research topic.
2. Accuracy and consistency with the provided findings.
3. Clear organization and readability.
4. Unsupported claims or invented sources.
5. Missing important information.

If the report is satisfactory, approve it.

If improvements are needed, correct the report and return the improved version.

Return your response in exactly this format:

APPROVED: YES or NO

REPORT:
The complete reviewed report.
"""

    response = llm.invoke(prompt)
    review = _normalize_response(response.content)
    approved = "APPROVED: YES" in review.upper()

    if "REPORT:" in review.upper():
        report_marker = review.upper().find("REPORT:")
        report = review[report_marker + len("REPORT:") :].strip()
    else:
        report = review.strip()

    return {"report": report, "approved": approved}

