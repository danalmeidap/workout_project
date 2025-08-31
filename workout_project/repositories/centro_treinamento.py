from typing import List, Optional

from models.centro_treinamento import CentroTreinamento
from schemas.centro_treinamento import (
    CentroTreinamentoCreate,
    CentroTreinamentoUpdate,
)
from sqlmodel import Session, select


def criar_centro_treinamento(
    db: Session, centro_in: CentroTreinamentoCreate
) -> CentroTreinamento:
    novo_centro = CentroTreinamento(**centro_in.model_dump())
    db.add(novo_centro)
    db.commit()
    db.refresh(novo_centro)
    return novo_centro


def obter_centro_treinamento_por_id(
    db: Session, centro_id: int
) -> Optional[CentroTreinamento]:
    return db.get(CentroTreinamento, centro_id)


def listar_centros_treinamento(db: Session) -> List[CentroTreinamento]:
    return db.exec(select(CentroTreinamento)).all()


def deletar_centro_treinamento(db: Session, centro_id: int) -> bool:
    centro = db.get(CentroTreinamento, centro_id)
    if centro:
        db.delete(centro)
        db.commit()
        return True
    return False


def atualizar_centro_treinamento(
    db: Session, centro_id: int, centro_update: CentroTreinamentoUpdate
) -> Optional[CentroTreinamento]:
    centro = db.get(CentroTreinamento, centro_id)
    if not centro:
        return None
    for key, value in centro_update.model_dump(exclude_unset=True).items():
        setattr(centro, key, value)
    db.add(centro)
    db.commit()
    db.refresh(centro)
    return centro
