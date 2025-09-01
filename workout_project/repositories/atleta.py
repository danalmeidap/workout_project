from typing import List, Optional

from sqlmodel import Session, select
from sqlmodel.ext.asyncio.session import AsyncSession

from workout_project.models.atleta import Atleta
from workout_project.schemas.atleta import AtletaIn, AtletaOut, AtletaUpdate


def criar_atleta(db: Session, atleta_in: AtletaIn) -> Atleta:
    novo_atleta = Atleta(**atleta_in.model_dump())
    db.add(novo_atleta)
    db.commit()
    db.refresh(novo_atleta)
    return novo_atleta


def obter_atleta_por_id(db: Session, atleta_id: int) -> Optional[Atleta]:
    return db.get(Atleta, atleta_id)


async def listar_atletas(db: AsyncSession) -> List[AtletaOut]:  # noqa: F821
    result = await db.exec(select(Atleta))
    atletas = result.all()
    return atletas


def deletar_atleta(db: Session, atleta_id: int) -> bool:
    atleta = db.get(Atleta, atleta_id)
    if atleta:
        db.delete(atleta)
        db.commit()
        return True
    return False


def atualizar_atleta(
    db: Session, atleta_id: int, atleta_update: AtletaUpdate
) -> Optional[Atleta]:
    atleta = db.get(Atleta, atleta_id)
    if not atleta:
        return None
    for key, value in atleta_update.model_dump(exclude_unset=True).items():
        setattr(atleta, key, value)

    db.add(atleta)
    db.commit()
    db.refresh(atleta)
    return atleta
