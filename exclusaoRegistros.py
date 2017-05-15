from criacaoBanco import *

sql = """
    DELETE FROM albums
    WHERE artist = 'John Doe'
    """
cursor.execute(sql)
conn.commit()
