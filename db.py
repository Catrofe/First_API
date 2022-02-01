from peewee import *
from playhouse.mysql_ext import MySQLConnectorDatabase
from typing import List, Dict, Any, Optional, Union

db = MySQLConnectorDatabase('biblioteca_manager', host='localhost', user='root', password='')

class BaseModel(Model):

    class Meta:
        database = db

class Livros(BaseModel):
    titulo = CharField(null=False, unique=True)
    editora = CharField(null=False)
    foto = CharField(null=False)
    autor = CharField(null=False)

class AlteraDB:
    def __init__(self):
        db.create_tables([Livros])

    def insere_livro(self, livro: Dict[str, Any]):
        db.connect()
        db.create_tables([Livros])
        print(livro)

        livro = Livros(titulo=livro['titulo'], editora=livro['editora'], foto=livro['foto'], autor=livro['autor'])
        livro.save()
        db.close()
    
    def livros_cadastrados(self):
        lista_de_livros = []
        for livro in Livros.select():
            lista_de_livros.append({
            'titulo': livro.titulo,
            'editora': livro.editora,
            'foto': livro.foto,
            'autor': livro.autor,
            'id': livro.id
            })
        return lista_de_livros

    def deleta_livro(self, id_livro: int):
        Livros.delete_by_id(id_livro)

    def atualiza_livro(self,id_livro, livro):
        # livro_encontrado = Livros.get_id(id_livro)
        q = (Livros.update({Livros.titulo: livro['titulo'], Livros.editora: livro['editora'], Livros.foto: livro['foto'], Livros.autor: livro['autor']})
            .where(Livros.id == id_livro))
        q.execute()