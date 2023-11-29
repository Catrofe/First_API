from typing import Any, Dict, List

from peewee import CharField, Model
from playhouse.mysql_ext import MySQLConnectorDatabase

db = MySQLConnectorDatabase(
    "biblioteca_manager", host="localhost", user="root", password=""
)


class BaseModel(Model):
    class Meta:
        database = db


class Livros(BaseModel):
    titulo = CharField(null=False, unique=True)
    editora = CharField(null=False)
    foto = CharField(null=False)
    autor = CharField(null=False)


class RepositorioLivros:
    def __init__(self):
        try:
            db.create_tables([Livros])
        except Exception:
            pass

    def insere_livro(self, livro: Dict[str, Any]) -> None:
        Livros.create(
            titulo=livro["titulo"],
            editora=livro["editora"],
            foto=livro["foto"],
            autor=livro["autor"],
        )

    def livros_cadastrados(self) -> List[Livros]:
        return [
            {
                "titulo": livro.titulo,
                "editora": livro.editora,
                "foto": livro.foto,
                "autor": livro.autor,
                "id": livro.id,
            }
            for livro in Livros.select()
        ]

    def deleta_livro(self, id_livro: int) -> None:
        Livros.delete_by_id(id_livro)

    def atualiza_livro(self, id_livro, livro) -> None:
        Livros.set_by_id(id_livro, livro)
