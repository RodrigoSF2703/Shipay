from models.user_claim import UserClaim
from datetime import date
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String, nullable=False)

    role_id: Mapped[int] = mapped_column(
        ForeignKey("roles.id"),
        nullable=False
    )

    created_at: Mapped[date] = mapped_column(nullable=False)
    updated_at: Mapped[date | None]

    role = relationship("Role", back_populates="users")

    claims = relationship(
        "Claim",
        secondary=UserClaim.__table__,
        back_populates="users"
    )

