from typing import List

from fastapi import APIRouter, Body, Depends, HTTPException, status
from sqlmodel.ext.asyncio.session import AsyncSession

from workout_project.db.dependencies import get_session
from workout_project.repositories.categoria import (
    atualizar_categoria,
    criar_categoria,
    deletar_categoria,
    listar_categorias,
    obter_categoria_por_id,
)
from workout_project.schemas.categoria import CategoriaIn, CategoriaOut

router = APIRouter(prefix="/categorias", tags=["Categorias"])


@router.get("/", response_model=List[CategoriaOut])
async def listar_todas_categorias(db: AsyncSession = Depends(get_session)):
    return await listar_categorias(db)


@router.get("/{categoria_id}", response_model=CategoriaOut)
async def obter_categoria(
    categoria_id: int, db: AsyncSession = Depends(get_session)
):
    categoria = await obter_categoria_por_id(db, categoria_id)
    if not categoria:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Categoria não encontrada",
        )
    return categoria


@router.post(
    "/", response_model=CategoriaOut, status_code=status.HTTP_201_CREATED
)
async def criar_nova_categoria(
    categoria_in: CategoriaIn = Body(...),
    db: AsyncSession = Depends(get_session),
):
    try:
        nova_categoria = await criar_categoria(db, categoria_in)
        return nova_categoria
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )


@router.put("/{categoria_id}", response_model=CategoriaOut)
async def atualizar_dados_categoria(
    categoria_id: int,
    categoria_update: CategoriaIn = Body(...),
    db: AsyncSession = Depends(get_session),
):
    categoria = await atualizar_categoria(db, categoria_id, categoria_update)
    if not categoria:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Categoria não encontrada",
        )
    return categoria


@router.delete("/{categoria_id}", status_code=status.HTTP_204_NO_CONTENT)
async def deletar_uma_categoria(
    categoria_id: int, db: AsyncSession = Depends(get_session)
):
    sucesso = await deletar_categoria(db, categoria_id)
    if not sucesso:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Categoria não encontrada",
        )
    # Retorna None para o status 204 No Content
    return None  # noqa: PLR1711
