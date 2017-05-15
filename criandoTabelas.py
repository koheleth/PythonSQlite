from criacaoBanco import *
# Criando tabela albuns

def criaTabelaAlbuns():
    cursor.execute("""CREATE TABLE albuns
                    (title text,
                    artist text,
                    release_date text,
                    publisher text,
                    media_type text)""")

criaTabelaAlbuns()
