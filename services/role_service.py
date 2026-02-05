from repositories.role_repository import RoleRepository
from sqlalchemy.ext.asyncio import AsyncSession
from models.role import Role


class RoleService:

    @staticmethod
    async def get_role_by_id(
        db: AsyncSession,
        role_id: int
    ) -> Role:
        role = await RoleRepository.get_by_id(db, role_id)

        if not role:
            raise ValueError("Role não encontrada")

        return role
