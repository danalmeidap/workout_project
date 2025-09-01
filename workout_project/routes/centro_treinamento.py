from typing import List

from fastapi import APIRouter, Body, Depends, HTTPException, status
from sqlmodel.ext.asyncio.session import AsyncSession

from workout_project.db.dependencies import get_session
from workout_project.repositories.centro_treinamento import (
    atualizar_centro_treinamento,
    criar_centro_treinamento,
    deletar_centro_treinamento,
    listar_centros_treinamento,
    obter_centro_treinamento_por_id,
)
from workout_project.schemas.centro_treinamento import (
    CentroTreinamentoIn,
    CentroTreinamentoOut,
)

router = APIRouter(
    prefix="/centros_treinamento", tags=["Centros de Treinamento"]
)  # noqa: E501


@router.get("/", response_model=List[CentroTreinamentoOut])
async def listar_todos_centros_treinamento(
    db: AsyncSession = Depends(get_session),
):  # noqa: E501
    return await listar_centros_treinamento(db)


@router.get("/{centro_id}", response_model=CentroTreinamentoOut)
async def obter_centro_treinamento(
    centro_id: int, db: AsyncSession = Depends(get_session)
):
    centro = await obter_centro_treinamento_por_id(db, centro_id)
    if not centro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Centro de Treinamento não encontrado",
        )
    return centro


@router.post(
    "/",
    response_model=CentroTreinamentoOut,
    status_code=status.HTTP_201_CREATED,  # noqa: E501
)
async def criar_novo_centro_treinamento(
    centro_in: CentroTreinamentoIn = Body(...),
    db: AsyncSession = Depends(get_session),
):
    try:
        nova_centro = await criar_centro_treinamento(db, centro_in)
        return nova_centro
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)
        )


@router.put("/{centro_id}", response_model=CentroTreinamentoOut)
async def atualizar_dados_centro_treinamento(
    centro_id: int,
    centro_update: CentroTreinamentoIn = Body(...),
    db: AsyncSession = Depends(get_session),
):
    centro = await atualizar_centro_treinamento(db, centro_id, centro_update)
    if not centro:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Centro de Treinamento não encontrado",
        )
    return centro


@router.delete("/{centro_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_centro_treinamento(
    centro_id: int, db: AsyncSession = Depends(get_session)
):  # noqa: E501
    sucesso = await deletar_centro_treinamento(db, centro_id)
    if not sucesso:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Centro de Treinamento não encontrado",
        )
    return None  # noqa: PLR1711
