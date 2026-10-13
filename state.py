from typing import TypedDict


class ResearchState(TypedDict):
    query: str
    plan: list[str]
    findings: list[str]
    analysis: str
    report: str
    approved: bool


