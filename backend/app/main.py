from fastapi import FastAPI

app = FastAPI(title="NBA Game Predictor API")

@app.get("/health")
def health():
    return {"ok": True}
