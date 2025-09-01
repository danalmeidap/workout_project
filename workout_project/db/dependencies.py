from sqlmodel.ext.asyncio.session import AsyncSession

from workout_project.db.engine import engine


async def get_session() -> AsyncSession:  # type: ignore
    """
    Dependência que fornece uma sessão assíncrona para as rotas.
    """
    async with AsyncSession(engine) as session:
        yield session
