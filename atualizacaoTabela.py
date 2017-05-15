from criacaoBanco import *
sql = """
        UPDATE albums
        SET artist = 'John Doe'
        WHERE artist = 'Andy Hunter'
        """
cursor.execute(sql)
conn.commit()
