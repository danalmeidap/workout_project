from contextlib import asynccontextmanager

from fastapi import FastAPI

from workout_project.db.engine import criar_banco
from workout_project.routes.atleta import router as atleta_router
from workout_project.routes.cateogia import router as categoria_router
from workout_project.routes.centro_treinamento import (
    router as centro_treinamento_router,
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await criar_banco()
    print("Banco de dados criado com sucesso.")
    yield


app = FastAPI(title="Workout Tracker API", lifespan=lifespan)
app.include_router(atleta_router)
app.include_router(categoria_router)
app.include_router(centro_treinamento_router)


@app.get("/")
async def root():
    return {"msg": "Workout Tracker API rodando!"}
