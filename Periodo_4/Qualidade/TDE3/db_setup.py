import sqlite3

# Conexão e criação do banco de dados
conn = sqlite3.connect('nao_conformidades.db')
cursor = conn.cursor()

# Criação da tabela de não-conformidades
cursor.execute('''
CREATE TABLE IF NOT EXISTS nao_conformidades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    descricao TEXT NOT NULL,
    responsavel TEXT NOT NULL,
    impacto TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'Aberta',
    aplicavel TEXT NOT NULL CHECK (aplicavel IN ('Sim', 'Não'))
)
''')

conn.commit()
conn.close()
print("Banco de dados e tabela criados com sucesso!")
