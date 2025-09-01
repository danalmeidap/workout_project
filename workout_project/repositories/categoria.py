from typing import List, Optional

from models.categoria import Categoria
from schemas.categoria import CategoriaCreate, CategoriaUpdate
from sqlmodel import Session, select


def criar_categoria(db: Session, categoria_in: CategoriaCreate) -> Categoria:
    nova_categoria = Categoria(**categoria_in.model_dump())
    db.add(nova_categoria)
    db.commit()
    db.refresh(nova_categoria)
    return nova_categoria


def obter_categoria_por_id(
    db: Session, categoria_id: int
) -> Optional[Categoria]:
    return db.get(Categoria, categoria_id)


def listar_categorias(db: Session) -> List[Categoria]:
    return db.exec(select(Categoria)).all()


def deletar_categoria(db: Session, categoria_id: int) -> bool:
    categoria = db.get(Categoria, categoria_id)
    if categoria:
        db.delete(categoria)
        db.commit()
        return True
    return False


def atualizar_categoria(
    db: Session, categoria_id: int, categoria_update: CategoriaUpdate
) -> Optional[Categoria]:
    categoria = db.get(Categoria, categoria_id)
    if not categoria:
        return None
    for key, value in categoria_update.model_dump(exclude_unset=True).items():
        setattr(categoria, key, value)
    db.add(categoria)
    db.commit()
    db.refresh(categoria)
    return categoria
