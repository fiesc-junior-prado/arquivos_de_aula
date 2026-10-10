from fastapi import FastAPI,Header, HTTPException
# from app.api.routes.games_routes import router as games_router
from app.api.routes import games_routes, returns_routes


app= FastAPI(title="Minha API", description="API de exemplo com FastAPI", version="1.0.0")

@app.get("/")
def root():
    return {"message": "Bem-vindo à minha API! Meus caros!"}

@app.get("/health")
def health():
    return {"API rodando normailmente!"}

#rota com path params
@app.get("/hello/{name}/{age}")
def hello(name:str,age:int):
    return {f'Olá {name} de {age} anos! Seja bem-vindo à minha API!'}

#rota com path params
@app.get("/hello")
def hello(name:str,age:int=18):
    return {f'Olá {name} de {age} anos! Seja bem-vindo à minha API!'}

## additional routes
app.include_router(games_routes.router)
app.include_router(returns_routes.router)

# Header params
@app.get("/teste-header")
def teste_header(
    user_agent: str | None = Header(default=None),
    token: str | None = Header(...)
    ):
    try:
        if token != "123ABC":
            raise HTTPException(status_code=400, detail="Token is required")
        
        return {"User-Agent": user_agent, "Token": token}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))