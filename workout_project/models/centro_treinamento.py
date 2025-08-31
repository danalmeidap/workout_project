from atleta import Atleta
from models import BaseModel
from sqlalchemy import String, integer, relantionship
from sqlalchemy.orm import Mapped, mapped_column


class CentroTreinamento(BaseModel):
    __tablename__ = "centro_treinamento"
    pk_id: Mapped[int] = mapped_column(
        integer, primary_key=True, autoincrement=True
    )
    nome: Mapped[str] = mapped_column(String(20), nullable=False)
    endereco: Mapped[str] = mapped_column(String(60), nullable=False)
    proprietario: Mapped[str] = mapped_column(String(30), nullable=False)
    atleta: Mapped["Atleta"] = relantionship(
        back_populates="centro_treinamento"
    )
