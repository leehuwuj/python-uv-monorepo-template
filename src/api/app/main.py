from app.routers.health import router as health_router
from fastapi import FastAPI


def create_app() -> FastAPI:
    app = FastAPI()

    app.include_router(health_router, prefix="/health", tags=["health"])

    return app


app = create_app()
