from fastapi import FastAPI


from app.database import (
    engine,
    Base
)


from app.models import (
    user,
    task
)


from app.routes.auth import (
    router as auth_router
)


from app.routes.tasks import (
    router as task_router
)

from app.routes.admin import (
    router as admin_router
)

Base.metadata.create_all(
    bind=engine
)


app = FastAPI(
    title="Backend Assignment API"
)


app.include_router(
    auth_router
)

app.include_router(
    admin_router
)

app.include_router(
    task_router
)


@app.get("/")
def root():

    return {
        "message": "Backend running"
    }