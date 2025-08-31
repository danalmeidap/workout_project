# tests/conftest.py
import pytest
from sqlmodel import SQLModel, create_engine
from sqlmodel.orm.session import Session

from workout_project.models.atleta import Atleta  # noqa: F401
from workout_project.models.categoria import Categoria  # noqa: F401
from workout_project.models.centro_treinamento import (
    CentroTreinamento,  # noqa: F401
)


@pytest.fixture(name="db")
def session_fixture():
    engine = create_engine("sqlite:///database.db")
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session
    SQLModel.metadata.drop_all(engine)
