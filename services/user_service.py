from datetime import date
from sqlalchemy.ext.asyncio import AsyncSession

from models.user import User
from schemas.user import UserCreate
from repositories.user_repository import UserRepository
from repositories.role_repository import RoleRepository
from core.security import (
    generate_random_password,
    get_password_hash,
)


class UserService:

    @staticmethod
    async def create_user(
        db: AsyncSession,
        user_data: UserCreate
    ) -> User:

        # Verifica se o email já existe
        existing_user = await UserRepository.get_by_email(
            db, user_data.email
        )
        if existing_user:
            raise ValueError("Email já cadastrado")

        # Verifica se o role existe
        role = await RoleRepository.get_by_id(
            db, user_data.role_id
        )
        if not role:
            raise ValueError("Role inválida")

        # Gera senha se não for informada
        raw_password = (
            user_data.password
            if user_data.password
            else generate_random_password()
        )

        hashed_password = get_password_hash(raw_password)

        # Cria o usuário
        user = User(
            name=user_data.name,
            email=user_data.email,
            password=hashed_password,
            role_id=user_data.role_id,
            created_at=date.today(),
        )

        return await UserRepository.create(db, user)
