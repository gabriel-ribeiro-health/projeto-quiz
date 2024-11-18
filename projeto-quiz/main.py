from fastapi import FastAPI # type: ignore
from api.vote_endpoints import router as vote_router

app = FastAPI()

# Registrar os endpoints do roteador
app.include_router(vote_router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Sistema Gamificado de Quiz"}
