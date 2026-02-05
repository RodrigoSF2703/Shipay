from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import get_db
from schemas.user import UserCreate, UserResponse
from services.user_service import UserService

router = APIRouter()


@router.post(
    "/users",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
async def create_user(
    user_data: UserCreate,
    db: AsyncSession = Depends(get_db)
):
    try:
        user = await UserService.create_user(db, user_data)
        return user
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
