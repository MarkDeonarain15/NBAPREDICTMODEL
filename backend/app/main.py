from fastapi import FastAPI

app = FastAPI(title="NBA Game Predictor API")


@app.get("/")
def root():
    return {"message": "NBA Predictor API Running"}


@app.get("/health")
def health():
    return {"ok": True}