from peewee import *
from playhouse.mysql_ext import MySQLConnectorDatabase
from typing import  Dict, Any, List

db = MySQLConnectorDatabase('biblioteca_manager', host='localhost', user='root', password='')

class BaseModel(Model):
    class Meta:
        database = db

class Livros(BaseModel):
    titulo = CharField(null=False, unique=True)
    editora = CharField(null=False)
    foto = CharField(null=False)
    autor = CharField(null=False)

class RepositorioLivros:
    # XXX Na segunda vez que rodamos a API isso quebra.
    # def __init__(self):
    #     db.create_tables([Livros])

    def insere_livro(self, livro: Dict[str, Any])->None:
        Livros.create(titulo=livro['titulo'], editora=livro['editora'], foto=livro['foto'], autor=livro['autor'])
    
    def livros_cadastrados(self)->List[Livros]:
        livros = []
        for livro in Livros.select():
            livros.append({
            'titulo': livro.titulo,
            'editora': livro.editora,
            'foto': livro.foto,
            'autor': livro.autor,
            'id': livro.id
            })
        return livros

    def deleta_livro(self, id_livro: int)->None:
        Livros.delete_by_id(id_livro)

    def atualiza_livro(self,id_livro, livro)->None:
        Livros.update(livro).where("id" == id_livro).execute()