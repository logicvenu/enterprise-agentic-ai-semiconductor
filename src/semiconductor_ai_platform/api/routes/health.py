from fastapi import APIRouter, Request

router = APIRouter(tags=["health"])


@router.get("/health/live", summary="Liveness probe")
async def liveness() -> dict[str, str]:
    """Indicate that the process is running; no dependency checks are performed."""
    return {"status": "alive"}


@router.get("/health/ready", summary="Readiness probe")
async def readiness(request: Request) -> dict[str, str]:
    """Initial readiness endpoint; dependency checks will be added with real adapters."""
    return {"status": "ready", "environment": request.app.state.settings.environment}
