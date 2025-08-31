from atleta import Atleta
from models import BaseModel
from sqlalchemy import String, integer, relantionship
from sqlalchemy.orm import Mapped, mapped_column


class Categoria(BaseModel):
    __tablename__ = "categorias"
    pk_id: Mapped[int] = mapped_column(
        integer, primary_key=True, autoincrement=True
    )
    nome: Mapped[str] = mapped_column(String(10), nullable=False)
    atleta: Mapped["Atleta"] = relantionship(back_populates="Categoria")
