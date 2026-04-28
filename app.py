# Sample backend (Python FastAPI placeholder)

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "DPDP Privacy Sentinel API running"}
