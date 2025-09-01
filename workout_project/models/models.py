from sqlalchemy import UUID
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class BaseModel(DeclarativeBase):
    id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True, default=UUID, nullable=False)
    )
