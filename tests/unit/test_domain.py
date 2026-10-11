import pytest
from pydantic import ValidationError

from semiconductor_ai_platform.domain.diagnosis import DiagnosisRequest, DiagnosisResult


def test_diagnosis_request_requires_actor_and_regression():
    request = DiagnosisRequest(regression_id="REG-78231", requested_by="engineer-001")
    assert request.regression_id == "REG-78231"
    assert request.project_id is None


def test_diagnosis_request_rejects_unknown_fields():
    with pytest.raises(ValidationError):
        DiagnosisRequest(
            regression_id="REG-78231",
            requested_by="engineer-001",
            unexpected="not-allowed",
        )


@pytest.mark.parametrize("confidence", [-0.1, 1.1])
def test_diagnosis_result_rejects_out_of_range_confidence(confidence):
    with pytest.raises(ValidationError):
        DiagnosisResult(
            regression_id="REG-78231",
            summary="Example",
            confidence=confidence,
        )
