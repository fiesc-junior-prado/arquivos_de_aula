from fastapi import APIRouter
from app.models.schemas import Game

router = APIRouter(prefix="/games", tags=["Games"])

games=[]

@router.post("/add", summary="Adiciona um novo jogo", description="Adiciona um novo jogo à lista de jogos")
def add_game(payload: Game):
    """
    Adiciona um novo jogo à lista de jogos.
    - **id**: ID do jogo
    - **name**: Nome do jogo
    - **genero**: Gênero do jogo
    - **plataforma**: Plataforma do jogo
    """
    games.append(payload)
    return {"message": "Jogo adicionado com sucesso!"}

@router.get("/list", summary="Lista todos os jogos", description="Retorna a lista de todos os jogos cadastrados")
def list_games():
    """
    Retorna a lista de todos os jogos cadastrados.
    """
    return games

