from collections.abc import Sequence
from typing import Any, Protocol

from semiconductor_ai_platform.domain.diagnosis import (
    DiagnosisRequest,
    DiagnosisResult,
    EvidenceItem,
)


class ModelGateway(Protocol):
    """Provider-neutral contract for model inference."""

    async def generate(self, *, prompt: str, metadata: dict[str, Any]) -> str: ...


class KnowledgeService(Protocol):
    """Authorization-aware knowledge retrieval contract."""

    async def retrieve(
        self, *, query: str, project_id: str | None, limit: int
    ) -> Sequence[EvidenceItem]: ...


class ToolGateway(Protocol):
    """Policy-enforcing gateway for engineering tool operations."""

    async def execute(
        self, *, tool_name: str, arguments: dict[str, Any], actor_id: str
    ) -> dict[str, Any]: ...


class AuditService(Protocol):
    """Append-only record of security-relevant actions and decisions."""

    async def record(self, *, event_type: str, attributes: dict[str, Any]) -> None: ...


class EvaluationService(Protocol):
    """Evaluate a result against an agreed evaluation contract."""

    async def evaluate(
        self, *, request: DiagnosisRequest, result: DiagnosisResult
    ) -> dict[str, Any]: ...
