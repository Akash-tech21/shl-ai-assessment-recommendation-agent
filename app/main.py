from fastapi import FastAPI
from app.api.chat import router

app = FastAPI(
    title="SHL Assessment Recommendation Agent",
    version="1.0.0"
)

app.include_router(router)

@app.get("/")
def root():
    return {"message": "SHL AI Agent is running"}

@app.get("/health")
def health():
    return {"status": "ok"}