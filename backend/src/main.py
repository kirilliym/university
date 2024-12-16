import asyncio
import logging
import uvicorn

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from project.core.config import settings
from project.controllers.healthcheck import healthcheck_router
from project.controllers.auth import auth_router
from project.controllers.university_db_controllers import ( 
    professor_router, faculte_router, kafedra_router, direction_router, grop_router, study_plan_router, subject_router,
    exam_router, grade_router, subject_in_study_router
)

logger = logging.getLogger(__name__)


def create_app() -> FastAPI:
    app_options = {}
    if settings.ENV.lower() == "prod":
        app_options = {
            "docs_url": None,
            "redoc_url": None,
        }
    if settings.LOG_LEVEL in ["DEBUG", "INFO"]:
        app_options["debug"] = True

    app = FastAPI(root_path=settings.ROOT_PATH, **app_options)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(auth_router, tags=["Auth"])
    app.include_router(healthcheck_router, tags=["Health check"])
    app.include_router(professor_router, tags=["Professors"])
    app.include_router(faculte_router, tags=["Faculties"])
    app.include_router(kafedra_router, tags=["Kafedras"])
    app.include_router(direction_router, tags=["Directions"])
    app.include_router(grop_router, tags=["Groups"])
    app.include_router(study_plan_router, tags=["Study Plans"])
    app.include_router(subject_router, tags=["Subjects"])
    app.include_router(exam_router, tags=["Exams"])
    app.include_router(grade_router, tags=["Grades"])
    app.include_router(subject_in_study_router, tags=["Subjects in Study"])

    return app


app = create_app()


async def run() -> None:
    config = uvicorn.Config("main:app", host="0.0.0.0", port=8000, reload=True)
    server = uvicorn.Server(config=config)
    tasks = (
        asyncio.create_task(server.serve()),
    )

    await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)


if __name__ == "__main__":
    logger.debug(f"{settings.postgres_url}=")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
