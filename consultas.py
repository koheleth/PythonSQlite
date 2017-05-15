from criacaoBanco import *

sql = "SELECT * FROM albuns WHERE artist=?"
cursor.execute(sql, ["Red"])
print(cursor.fetchall())  # ou use fetchone()

print("\nAqui a lista de todos os registros na tabela:\n")
for row in cursor.execute("SELECT rowid, * FROM albuns ORDER BY artist"):
    print(row)

print("\nResultados de uma consulta com LIKE:\n")

sql = """
    SELECT * FROM albuns
    WHERE title LIKE 'The%'
    """

cursor.execute(sql)
print(cursor.fetchall())
