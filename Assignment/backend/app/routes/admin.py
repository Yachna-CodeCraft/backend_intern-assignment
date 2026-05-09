from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi.security import HTTPBearer
from fastapi.security import HTTPAuthorizationCredentials

from sqlalchemy.orm import Session

from app.database import get_db

from app.models.user import User

from app.core.security import decode_token


router = APIRouter(
    prefix="/api/v1/admin",
    tags=["Admin"]
)


security = HTTPBearer()


def admin_only(
    credentials: HTTPAuthorizationCredentials = Depends(
        security
    )
):

    token = credentials.credentials

    payload = decode_token(
        token
    )

    if payload["role"] != "admin":

        raise HTTPException(
            status_code=403,
            detail="Admin access required"
        )

    return payload


@router.get("/users")
def get_all_users(

    current_user = Depends(
        admin_only
    ),

    db: Session = Depends(
        get_db
    )
):

    users = db.query(
        User
    ).all()

    return users