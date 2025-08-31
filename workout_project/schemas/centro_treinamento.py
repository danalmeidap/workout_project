from typing import Annotated

from pydantic import Field
from schemas.schemas import BaseSchema


class CentroTreinamento(BaseSchema):
    nome: Annotated[
        str,
        Field(
            description="Nome do centro de treinamento",
            example="Fit Center",
            max_lenghth=20,
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
    proprietatio: Annotated[
        str,
        Field(
            description="Proprietario do centro de treinamento",
            example="Joao Silva",
            max_length=30,
        ),
    ]
