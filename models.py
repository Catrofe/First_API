from pydantic import BaseModel
from typing import List, Dict, Any, Optional

class ModeloDoItem(BaseModel): 
    titulo: str
    editora: str
    foto: str
    autor: str

class ModeloDoItemResposta(ModeloDoItem):
    id: int
