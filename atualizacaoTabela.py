from criacaoBanco import *
sql = """
        UPDATE albuns
        SET artist = 'John Doe'
        WHERE artist = 'Andy Hunter'
        """
cursor.execute(sql)
conn.commit()
