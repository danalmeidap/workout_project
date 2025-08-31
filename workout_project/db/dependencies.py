from sqlmodel import Session

from workout_project.db import engine


def get_session():
    with Session(engine) as session:
        yield session
