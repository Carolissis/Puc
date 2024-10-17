import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk

# Conexão com o banco de dados
def conectar():
    return sqlite3.connect('nao_conformidades.db')

# Criação do banco e tabela se não existir
def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
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

# Função para adicionar uma nova não-conformidade
def adicionar_nao_conformidade():
    descricao = descricao_entry.get()
    responsavel = responsavel_entry.get()
    impacto = impacto_entry.get()
    aplicavel = aplicavel_combo.get()

    if not descricao or not responsavel or not impacto or aplicavel not in ['Sim', 'Não']:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos corretamente.")
        return

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO nao_conformidades (descricao, responsavel, impacto, aplicavel)
        VALUES (?, ?, ?, ?)
    ''', (descricao, responsavel, impacto, aplicavel))
    conn.commit()
    conn.close()
    messagebox.showinfo("Sucesso", "Não-conformidade adicionada com sucesso!")
    listar_nao_conformidades()

# Função para listar todas as não-conformidades
def listar_nao_conformidades():
    for item in tree.get_children():
        tree.delete(item)

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM nao_conformidades')
    registros = cursor.fetchall()
    conn.close()

    for reg in registros:
        tree.insert("", "end", values=reg)

# Função para atualizar o status de uma não-conformidade
def atualizar_status():
    selecionado = tree.focus()
    if not selecionado:
        messagebox.showwarning("Aviso", "Selecione uma não-conformidade para atualizar.")
        return

    id = tree.item(selecionado)['values'][0]
    novo_status = status_combo.get()

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('UPDATE nao_conformidades SET status = ? WHERE id = ?', (novo_status, id))
    conn.commit()
    conn.close()
    messagebox.showinfo("Sucesso", "Status atualizado com sucesso!")
    listar_nao_conformidades()

# Função para excluir uma não-conformidade
def excluir_nao_conformidade():
    selecionado = tree.focus()
    if not selecionado:
        messagebox.showwarning("Aviso", "Selecione uma não-conformidade para excluir.")
        return

    id = tree.item(selecionado)['values'][0]

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM nao_conformidades WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    messagebox.showinfo("Sucesso", "Não-conformidade excluída!")
    listar_nao_conformidades()

# Função para calcular a porcentagem de aderência
def calcular_aderencia():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM nao_conformidades WHERE aplicavel = "Sim"')
    total_aplicaveis = cursor.fetchone()[0]

    cursor.execute('''
        SELECT COUNT(*) FROM nao_conformidades 
        WHERE aplicavel = "Sim" AND LOWER(status) = "resolvida"
    ''')
    resolvidas = cursor.fetchone()[0]
    conn.close()

    if total_aplicaveis == 0:
        messagebox.showinfo("Aderência", "Nenhuma não-conformidade aplicável registrada.")
        return

    porcentagem = (resolvidas / total_aplicaveis) * 100
    classificacao = "Alta" if porcentagem >= 80 else "Média" if porcentagem >= 50 else "Baixa"
    messagebox.showinfo("Aderência", f"Aderência: {porcentagem:.2f}%\nClassificação: {classificacao}")

# Interface Tkinter
root = tk.Tk()
root.title("Sistema de Acompanhamento de Não-Conformidades")

# Widgets de entrada
tk.Label(root, text="Descrição").grid(row=0, column=0)
descricao_entry = tk.Entry(root)
descricao_entry.grid(row=0, column=1)

tk.Label(root, text="Responsável").grid(row=1, column=0)
responsavel_entry = tk.Entry(root)
responsavel_entry.grid(row=1, column=1)

tk.Label(root, text="Impacto").grid(row=2, column=0)
impacto_entry = tk.Entry(root)
impacto_entry.grid(row=2, column=1)

tk.Label(root, text="Aplicável").grid(row=3, column=0)
aplicavel_combo = ttk.Combobox(root, values=["Sim", "Não"])
aplicavel_combo.grid(row=3, column=1)

# Botões
tk.Button(root, text="Adicionar", command=adicionar_nao_conformidade).grid(row=4, column=0, columnspan=2)
tk.Button(root, text="Calcular Aderência", command=calcular_aderencia).grid(row=5, column=0, columnspan=2)

# Treeview para exibir as não-conformidades
tree = ttk.Treeview(root, columns=("ID", "Descrição", "Responsável", "Impacto", "Status", "Aplicável"), show="headings")
tree.grid(row=6, column=0, columnspan=2)
for col in tree["columns"]:
    tree.heading(col, text=col)

# Widgets para atualizar status
tk.Label(root, text="Novo Status").grid(row=7, column=0)
status_combo = ttk.Combobox(root, values=["Aberta", "Em Andamento", "Resolvida"])
status_combo.grid(row=7, column=1)

tk.Button(root, text="Atualizar Status", command=atualizar_status).grid(row=8, column=0, columnspan=2)
tk.Button(root, text="Excluir", command=excluir_nao_conformidade).grid(row=9, column=0, columnspan=2)

# Inicializar a tabela e o banco de dados
criar_tabela()
listar_nao_conformidades()

# Iniciar o loop da interface
root.mainloop()
