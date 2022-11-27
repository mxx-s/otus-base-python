from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello":"World"}


@app.get("/ping")
def get_pong():
    return {"message": "pong"}