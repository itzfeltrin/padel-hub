from fastapi import FastAPI
from app.core.config import settings
from app.api.main import router as api_router

def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.app_name,
        debug=settings.debug,
    )
    app.include_router(api_router, prefix=settings.api_v1_prefix, tags=["v1"])
    return app

app = create_app()