import asyncio
from logging.config import fileConfig

from sqlalchemy import pool
from sqlalchemy.engine import Connection
from sqlalchemy.ext.asyncio import async_engine_from_config

from alembic import context
from sqlmodel import SQLModel

# importa os models para o metadata ser detectado
from workout_project.models.atleta import Atleta
from workout_project.models.categoria import Categoria
from workout_project.models.centro_treinamento import CentroTreinamento

# Config do Alembic
config = context.config
fileConfig(config.config_file_name)

# aqui usamos o metadata do SQLModel
target_metadata = SQLModel.metadata


def get_url():
    # pega a URL do banco igual ao seu engine.py
    return "postgresql+asyncpg://workout:workout@localhost:5432/workout"


def run_migrations_offline():
    """Executa migrations no modo offline."""
    url = get_url()
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection: Connection):
    context.configure(
        connection=connection,
        target_metadata=target_metadata,
        compare_type=True,  # detecta mudanças em colunas (ex: String(50) -> String(100))
    )

    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online():
    """Executa migrations no modo online (async)."""
    connectable = async_engine_from_config(
        config.get_section(config.config_ini_section),
        url=get_url(),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)


def run_migrations():
    if context.is_offline_mode():
        run_migrations_offline()
    else:
        asyncio.run(run_migrations_online())


run_migrations()
