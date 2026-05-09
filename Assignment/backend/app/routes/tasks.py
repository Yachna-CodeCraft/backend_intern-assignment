from fastapi import APIRouter
from fastapi import Depends
from fastapi.security import HTTPBearer
from fastapi.security import HTTPAuthorizationCredentials

from sqlalchemy.orm import Session

from app.database import get_db
from app.models.task import Task
from app.schemas.task import TaskCreate

from app.core.security import decode_token


router = APIRouter(
    prefix="/api/v1/tasks",
    tags=["Tasks"]
)


security = HTTPBearer()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(
        security
    )
):

    token = credentials.credentials

    payload = decode_token(
        token
    )

    return payload


@router.post("/")
def create_task(

    task: TaskCreate,

    current_user=Depends(
        get_current_user
    ),

    db: Session = Depends(
        get_db
    )
):

    new_task = Task(
        title=task.title,
        description=task.description,
        owner_id=int(
            current_user["sub"]
        )
    )

    db.add(
        new_task
    )

    db.commit()

    return {
        "message": "Task created"
    }


@router.get("/")
def get_tasks(

    current_user=Depends(
        get_current_user
    ),

    db: Session = Depends(
        get_db
    )
):

    tasks = db.query(
        Task
    ).filter(
        Task.owner_id == int(
            current_user["sub"]
        )
    ).all()

    return tasks