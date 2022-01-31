from pydantic import BaseModel

class ModeloDoItem(BaseModel): 
    titulo: str
    editora: str
    foto: str
    autor: str

class ModeloDoItemResposta(ModeloDoItem):
    id: int
