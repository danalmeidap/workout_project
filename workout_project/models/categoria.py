from __future__ import annotations

from typing import List

from sqlmodel import Field, Relationship, SQLModel


class Categoria(SQLModel, table=True):
    __tablename__ = "categorias"
    pk_id: int | None = Field(default=None, primary_key=True)
    nome: str = Field(max_length=10, unique=True, nullable=False)
    atleta: List["Atleta"] = Relationship(back_populates="categoria")  # type: ignore # noqa: F821
