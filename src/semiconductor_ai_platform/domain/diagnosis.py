from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class DiagnosisRequest(BaseModel):
    """Input contract for a future regression-diagnosis workflow."""

    model_config = ConfigDict(extra="forbid")

    regression_id: str = Field(min_length=1, max_length=100, examples=["REG-78231"])
    project_id: str | None = Field(default=None, max_length=100)
    requested_by: str = Field(min_length=1, max_length=200)


class EvidenceItem(BaseModel):
    """A source-backed item supporting a diagnosis claim."""

    source_id: str
    source_type: Literal["regression", "test_log", "knowledge_document", "rtl", "coverage"]
    excerpt: str
    source_version: str | None = None


class DiagnosisResult(BaseModel):
    """Structured diagnosis result; confidence is not a substitute for evidence."""

    regression_id: str
    summary: str
    failure_pattern: str | None = None
    likely_root_cause: str | None = None
    confidence: float = Field(ge=0.0, le=1.0)
    evidence: list[EvidenceItem] = Field(default_factory=list)
    requires_human_review: bool = True
