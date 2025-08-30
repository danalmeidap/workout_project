from datetime import datetime

from models import BaseModel
from sqlalchemy import DateTime, String, integer
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
