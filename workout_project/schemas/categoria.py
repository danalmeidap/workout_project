from typing import Annotated

from pydantic import Field
from schemas.schemas import BaseSchema


class Categoria(BaseSchema):
    nome: Annotated[
        str,
        Field(
            description="Nome da categoria", example="Iniciante", max_length=10
        ),
    ]
