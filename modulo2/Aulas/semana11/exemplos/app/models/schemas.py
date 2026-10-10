from pydantic import BaseModel

class Game(BaseModel):
    id: int
    name: str
    genero: str
    plataforma: str