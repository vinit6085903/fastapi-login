from fastapi import FastAPI
from database import engine

app = FastAPI()

@app.get("/")
def home():
    try:
        engine.connect()
        return {"status": " MySQL LIVE connected successfully"}
    except Exception as e:
        return {"error": str(e)}
