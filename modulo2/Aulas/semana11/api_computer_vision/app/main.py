import uvicorn
from fastapi import FastAPI
from app.api.routes import conversion, visualization, classification, detection
from contextlib import asynccontextmanager

# Importação do serviço YOLO para pré-carregamento
from app.services.detection import load_models, clear_models

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Executado no startup
    try:
        load_models()
        yield
    finally:
        # Executado no shutdown
        print("Limpando modelos da memória...")
        clear_models()

app = FastAPI(
    title="Minha Api Visão Computacional",
    description="Api para detecção de objetos ",
    lifespan=lifespan
)

@app.get("/", tags=["Health"])
async def health():
    return {"status": "ok"}

#adicionando rotas
app.include_router(conversion.router)
app.include_router(visualization.router)
app.include_router(classification.router)
app.include_router(detection.router)

if __name__ == "__main__":
    # Configurações de inicialização do servidor Uvicorn
    uvicorn.run(
        host="0.0.0.0",       # Escuta em todas as interfaces de rede
        port=8000,            # Porta padrão da aplicação
        reload=True,          # Ativa o live-reload (ideal para desenvolvimento)
    )