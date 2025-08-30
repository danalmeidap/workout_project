from fastapi import FastAPI

app = FastAPI("Workout Tracker API")


@app.get("/")
def read_root():
    return {"message": "Welcome to the Workout Tracker API!"}
