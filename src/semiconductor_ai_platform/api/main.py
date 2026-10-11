from fastapi import FastAPI

from semiconductor_ai_platform.api.routes.health import router as health_router
from semiconductor_ai_platform.config.settings import get_settings
from semiconductor_ai_platform.observability.request_context import RequestIdMiddleware


def create_app() -> FastAPI:
    settings = get_settings()
    app = FastAPI(
        title=settings.app_name,
        version=settings.service_version,
        description=(
            "Foundation API for a governed semiconductor engineering AI platform. "
            "Diagnosis execution is not enabled in this build."
        ),
    )
    app.state.settings = settings

    if settings.enable_request_id_middleware:
        app.add_middleware(RequestIdMiddleware)

    app.include_router(health_router)
    return app


app = create_app()
