from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Render is working"}

@app.get("/health")
def health():
    return {"status": "ok"}