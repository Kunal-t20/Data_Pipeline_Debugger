from fastapi import FastAPI
from src.api.routes.debug import router as debug_router

app = FastAPI(title="ML Pipeline Debugger")

app.include_router(debug_router)


@app.get("/health")
def health():
    return {"status": "ok"}
