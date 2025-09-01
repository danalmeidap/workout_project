from typing import List

from fastapi import APIRouter, Body, Depends, HTTPException, status
from sqlmodel.ext.asyncio.session import AsyncSession

from workout_project.db.dependencies import get_session
from workout_project.repositories.atleta import (
    atualizar_atleta,
    criar_atleta,
    deletar_atleta,
    listar_atletas,
    obter_atleta_por_id,
)
from workout_project.schemas.atleta import AtletaIn, AtletaOut

router = APIRouter(prefix="/atletas", tags=["Atletas"])


@router.get("/", response_model=List[AtletaOut])
async def listar_todos_atletas(db: AsyncSession = Depends(get_session)):
    # Await para a função assíncrona do repositório
    return await listar_atletas(db)


@router.get("/{atleta_id}", response_model=AtletaOut)
async def obter_atleta(
    atleta_id: int, db: AsyncSession = Depends(get_session)
):
    # Await para a função assíncrona do repositório
    atleta = await obter_atleta_por_id(db, atleta_id)
    if not atleta:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Atleta não encontrado",
        )
    return atleta


@router.post(
    "/", response_model=AtletaOut, status_code=status.HTTP_201_CREATED
)
async def criar_novo_atleta(
    atleta_in: AtletaIn = Body(...),
    db: AsyncSession = Depends(get_session),
):
    try:
        # Await para a função assíncrona do repositório
        novo_atleta = await criar_atleta(db, atleta_in)
        return novo_atleta
    except Exception as e:
        # Mensagem de erro mais específica
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )


@router.put("/{atleta_id}", response_model=AtletaOut)
async def atualizar_dados_atleta(
    atleta_id: int,
    atleta_update: AtletaIn = Body(...),
    db: AsyncSession = Depends(get_session),
):
    # Await para a função assíncrona do repositório
    atleta_atualizado = await atualizar_atleta(db, atleta_id, atleta_update)
    if not atleta_atualizado:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Atleta não encontrado",
        )
    return atleta_atualizado


@router.delete("/{atleta_id}", status_code=status.HTTP_204_NO_CONTENT)
async def deletar_atleta_por_id(
    atleta_id: int, db: AsyncSession = Depends(get_session)
):
    # Await para a função assíncrona do repositório
    sucesso = await deletar_atleta(db, atleta_id)
    if not sucesso:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Atleta não encontrado",
        )
    # Retorna None para o status 204 No Content
    return None  # noqa: PLR1711
