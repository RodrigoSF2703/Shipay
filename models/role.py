from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.base import Base


class Role(Base):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str] = mapped_column(String, nullable=False)

    users = relationship("User", back_populates="role")
