import uvicorn
from fastapi import FastAPI
from app.api.routes import conversion, visualization

app = FastAPI(
    title="Minha Api Visão Computacional",
    description="Api para detecção de objetos ",
)

@app.get("/", tags=["Health"])
async def health():
    return {"status": "ok"}

#adicionando rotas
app.include_router(conversion.router)
app.include_router(visualization.router)

if __name__ == "__main__":
    # Configurações de inicialização do servidor Uvicorn
    uvicorn.run(
        host="0.0.0.0",       # Escuta em todas as interfaces de rede
        port=8000,            # Porta padrão da aplicação
        reload=True,          # Ativa o live-reload (ideal para desenvolvimento)
    )