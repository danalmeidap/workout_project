from datetime import datetime

from categoria import Categoria
from centro_treinamento import CentroTreinamento
from models import BaseModel
from sqlalchemy import DateTime, ForeignKey, String, integer, relantionship
from sqlalchemy.orm import Mapped, mapped_column


class Atleta(BaseModel):
    __tablename__ = "atletas"
    pk_id: Mapped[int] = mapped_column(
        integer, primary_key=True, autoincrement=True
    )
    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    cpf: Mapped[str] = mapped_column(String(11), unique=True, nullable=False)
    idade: Mapped[int] = mapped_column(integer, nullable=False)
    peso: Mapped[float] = mapped_column(float, nullable=False)
    altura: Mapped[float] = mapped_column(float, nullable=False)
    sexo: Mapped[str] = mapped_column(String(1), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    Categoria: Mapped["Categoria"] = relantionship(back_populates="Atletas")
    categoria_id: Mapped[int] = mapped_column(
        integer, ForeignKey("categorias.pk_id"), nullable=False
    )
    centro_treinamento: Mapped["CentroTreinamento"] = relantionship(
        back_populates="atleta"
    )
    centro_treinamento_id: Mapped[int] = mapped_column(
        integer, ForeignKey("centro_treinamento.pk_id"), nullable=False
    )
