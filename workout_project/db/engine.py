from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel import SQLModel

DATABASE_URL = "postgresql+asyncpg://workout:workout@localhost:5432/workout"

engine = create_async_engine(DATABASE_URL, echo=True, future=True)


async def criar_banco():
    """Cria as tabelas no banco de dados a partir dos modelos SQLModel."""
    # importa dentro da função para evitar problemas de import circular

    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
