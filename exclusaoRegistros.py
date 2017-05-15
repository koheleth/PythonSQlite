from criacaoBanco import *

sql = """
    DELETE FROM albuns
    WHERE artist = 'Andy Hunter'
    """
cursor.execute(sql)
conn.commit()
