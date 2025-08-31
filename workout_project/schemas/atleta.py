from datetime import datetime
from typing import Annotated

from pydantic import Field, PositiveFloat

# Importe a classe BaseSchema do seu projeto
from schemas import BaseSchema


class AtletaBase(BaseSchema):
    nome: Annotated[
        str,
        Field(
            description="Nome do atleta",
            example="João Silva",
            min_length=3,
            max_length=50,
        ),
    ]
    cpf: Annotated[
        str,
        Field(
            description="CPF do atleta",
            example="12345678900",
            max_length=11,
        ),
    ]
    idade: Annotated[int, Field(description="Idade do atleta", example=25)]
    peso: Annotated[
        PositiveFloat, Field(description="Peso do atleta em kg", example=70.5)
    ]
    altura: Annotated[
        PositiveFloat,
        Field(description="Altura do atleta em metros", example=1.75),
    ]
    sexo: Annotated[
        str, Field(description="Sexo do atleta", example="M", max_length=1)
    ]


class AtletaCreate(AtletaBase):
    pass


class AtletaIn(AtletaBase):
    categoria_id: Annotated[
        int, Field(description="ID da Categoria", example=1)
    ]
    centro_treinamento_id: Annotated[
        int, Field(description="ID do Centro de Treinamento", example=1)
    ]


class AtletaOut(AtletaBase):
    id: Annotated[str, Field(description="Identificador do Atleta")]
    created_at: Annotated[datetime, Field(description="Data de criação")]


class AtletaUpdate(BaseSchema):
    nome: Annotated[
        str,
        Field(
            description="Nome do atleta",
            example="João Silva",
            min_length=3,
            max_length=50,
        ),
    ]
    peso: Annotated[
        PositiveFloat, Field(description="Peso do atleta em kg", example=75.0)
    ]
    idade: Annotated[int, Field(description="Idade do atleta", example=26)]
