from datetime import date
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from models.role import Role
from models.user import User
from core.security import get_password_hash


async def seed_database(db: AsyncSession):
    # ===== Roles =====
    roles_data = [
        {"id": 1, "description": "ADMIN"},
        {"id": 2, "description": "USER"},
    ]

    for role_data in roles_data:
        result = await db.execute(
            select(Role).where(Role.id == role_data["id"])
        )
        if not result.scalar_one_or_none():
            db.add(Role(**role_data))

    await db.commit()

    # ===== Users =====
    users_data = [
        {
            "name": "Admin Test",
            "email": "admin@test.com",
            "password": get_password_hash("admin123"),
            "role_id": 1,
            "created_at": date.today(),
        },
        {
            "name": "User Test",
            "email": "user@test.com",
            "password": get_password_hash("user123"),
            "role_id": 2,
            "created_at": date.today(),
        },
    ]

    for user_data in users_data:
        result = await db.execute(
            select(User).where(User.email == user_data["email"])
        )
        if not result.scalar_one_or_none():
            db.add(User(**user_data))

    await db.commit()
