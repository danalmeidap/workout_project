from contextlib import asynccontextmanager

from fastapi import FastAPI

from workout_project.db.engine import criar_banco


@asynccontextmanager
async def lifespan(app: FastAPI):
    await criar_banco()
    print("Banco de dados criado com sucesso.")
    yield


app = FastAPI(title="Workout Tracker API", lifespan=lifespan)


@app.get("/")
async def root():
    return {"msg": "Workout Tracker API rodando!"}
