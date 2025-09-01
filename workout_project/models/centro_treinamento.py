from __future__ import annotations

from datetime import datetime
from typing import List

from sqlmodel import Field, Relationship, SQLModel


class CentroTreinamento(SQLModel, table=True):
    __tablename__ = "centro_treinamento"
    pk_id: int | None = Field(default=None, primary_key=True)
    nome: str = Field(max_length=20, unique=True, nullable=False)
    endereco: str = Field(max_length=60, nullable=False)
    proprietario: str = Field(max_length=30, nullable=False)
    created_at: datetime = Field(
        nullable=False, default_factory=datetime.utcnow
    )
    atletas: list["Atleta"] = Relationship(back_populates="centro_treinamento")  # type: ignore # noqa: F821
