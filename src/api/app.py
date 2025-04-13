from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routes import document

app = FastAPI(
    title="API",
    description="API sistema RAG",
    version="0.1.0",
)

# Configuração de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclusão dos routers
app.include_router(document.router)


@app.get("/")
async def root():
    """Endpoint raiz da API"""
    return {"message": "Bem-vindo à API do sistema RAG"}



