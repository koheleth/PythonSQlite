from criacaoBanco import *

# Para incluir apenas um registro
cursor.execute("INSERT INTO albuns VALUES ('Glow', 'Andy Hunter', '7/24/2017', 'Xplore Records', 'MP3')")

# Para inclusão de vários registros, usa-se uma lista composta de tuplas
albums = [('Exodus', 'Andy Hunter', '7/9/2002', 'Sparrow Records', 'CD'),
    ('Until We Have Faces', 'Red', '2/1/2011', 'Essential Records', 'CD'),
    ('The End is Where We Begin', 'Thousand Foot Krutch', '4/17/2012','TFKmusic', 'CD'),
    ('The Good Life', 'Trip Lee', '4/10/2012', 'Reach Records', 'CD')]

cursor.executemany("INSERT INTO albums VALUES (?,?,?,?,?)", albums)
conn.commit()
