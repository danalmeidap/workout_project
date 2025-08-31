from typing import Annotated

from pydantic import Field
from schemas.schemas import BaseSchema


class CategoriaBase(BaseSchema):
    nome: Annotated[
        str,
        Field(
            description="Nome da categoria", example="Iniciante", max_length=10
        ),
    ]


class CategoriaCreate(CategoriaBase):
    pass


class CategoriaOut(CategoriaBase):
    id: Annotated[int, Field(description="Identificador da categoria")]
