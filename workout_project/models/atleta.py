from __future__ import annotations
from datetime import datetime
from sqlmodel import Field, Relationship, SQLModel
from sqlalchemy.sql.sqltypes import Float

class Atleta(SQLModel, table=True):
    __tablename__ = "atletas"

    pk_id: int | None = Field(default=None, primary_key=True)
    nome: str = Field(max_length=50, nullable=False)
    cpf: str = Field(max_length=11, unique=True, nullable=False)
    idade: int = Field(nullable=False)
    peso: float = Field(nullable=False)
    altura: float = Field(nullable=False)
    sexo: str = Field(max_length=1, nullable=False)
    created_at: datetime = Field(nullable=False, default_factory=datetime.utcnow)

    categoria_id: int | None = Field(default=None, foreign_key="categorias.pk_id")
    categoria: "Categoria" | None = Relationship(back_populates="atletas")

    centro_treinamento_id: int | None = Field(default=None, foreign_key="centro_treinamento.pk_id")
    centro_treinamento: "CentroTreinamento" | None = Relationship(back_populates="atletas")
