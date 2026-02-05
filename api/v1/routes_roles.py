from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import get_db
from schemas.role import RoleResponse
from services.role_service import RoleService

router = APIRouter()


@router.get(
    "/roles/{role_id}",
    response_model=RoleResponse,
    status_code=status.HTTP_200_OK
)
async def get_role_by_id(
    role_id: int,
    db: AsyncSession = Depends(get_db)
):
    try:
        role = await RoleService.get_role_by_id(db, role_id)
        return role
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )
