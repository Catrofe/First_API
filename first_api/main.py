from fastapi import FastAPI
from first_api.db import RepositorioLivros
from first_api.models import ModeloDoItem, ModeloDoItemResposta

pw = RepositorioLivros()
app = FastAPI()


@app.get("/livros")
def index():
    return pw.livros_cadastrados()


@app.post("/livros/", response_model=ModeloDoItemResposta, status_code=201)
def cadastra_livro(item_a_inserir: ModeloDoItem):
    return pw.insere_livro(item_a_inserir.dict())


@app.put("/livros/{id_do_livro}", response_model=ModeloDoItemResposta)
def atualiza_livro(id_do_livro, obra: ModeloDoItem):
    return pw.atualiza_livro(id_do_livro, obra.dict())


@app.delete("/livros/{id_do_livro}", response_model=ModeloDoItemResposta)
def deleta_livro(id_do_livro):
    return pw.deleta_livro(id_do_livro)
