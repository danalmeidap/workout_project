from typing import Annotated

from pydantic import Field
from schemas.schemas import BaseSchema


class CentroTreinamentoBase(BaseSchema):
    nome: Annotated[
        str,
        Field(
            description="Nome do centro de treinamento",
            example="Fit Center",
            max_length=20,
        ),
    ]
    endereco: Annotated[
        str,
        Field(
            description="Endereço do centro de treinamento",
            example="Rua A, 123",
            max_length=60,
        ),
    ]
    proprietario: Annotated[
        str,
        Field(
            description="Proprietário do centro de treinamento",
            example="João Silva",
            max_length=30,
        ),
    ]


class CentroTreinamentoCreate(CentroTreinamentoBase):
    pass


class CentroTreinamentoOut(CentroTreinamentoBase):
    id: Annotated[int, Field(
        description="Identificador do centro de treinamento")
    ]