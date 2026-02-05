from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from models.role import Role


class RoleRepository:

    @staticmethod
    async def get_by_id(
        db: AsyncSession,
        role_id: int
    ) -> Role | None:
        result = await db.execute(
            select(Role).where(Role.id == role_id)
        )
        return result.scalar_one_or_none()
