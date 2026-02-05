from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column
from models.base import Base


class UserClaim(Base):
    __tablename__ = "user_claims"

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        primary_key=True
    )
    claim_id: Mapped[int] = mapped_column(
        ForeignKey("claims.id"),
        primary_key=True
    )

    __table_args__ = (
        UniqueConstraint("user_id", "claim_id"),
    )
