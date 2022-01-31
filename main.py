from fastapi import FastAPI
from typing import List, Dict, Any, Optional
from db import AlteraDB
from models import ModeloDoItem, ModeloDoItemResposta

pw = AlteraDB()
app = FastAPI()

@app.get("/obras")
def index():
    return pw.livros_cadastrados()

@app.post("/obras/", response_model=ModeloDoItemResposta, status_code=201)
def cadastra_obra(item_a_inserir: ModeloDoItem):
    return pw.inseri_livros(item_a_inserir.dict())

@app.put("/obras-att/{id_do_livro}", response_model=ModeloDoItemResposta)
def atualizar_obra(id_do_livro, obra: ModeloDoItem):
    return pw.atualiza_livro(id_do_livro, obra.dict())

@app.delete("/obras-del/{id_do_livro}", response_model=ModeloDoItemResposta)
def deleta_obra(id_do_livro):
    return pw.deleta_livro(id_do_livro)