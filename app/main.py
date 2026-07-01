from fastapi import FastAPI

from app.api.chat import router

app = FastAPI(
    title="SHL AI Agent"
)

app.include_router(router)


@app.get("/health")
def health():

    return {"status": "ok"}