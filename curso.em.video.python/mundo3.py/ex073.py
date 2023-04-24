#  Lista de nomes; mostras os cinco primeiros;
#  os quatro ultimos; deixar em ordem alfabetica;
#  mostrar qual a posição de tal elemento

nomes = ('Giovanna', 'Ricardo', 'Cadu', 'Marina', 'Guilherme', 'Carol', 'Isabella', 'Ana Maria',
         'Henrique', 'Tiago', 'Victor', 'Leonardo', 'Daniela', 'Lorenzo', 'Clara', 'Eduarda',
         'Livia', 'Roberto', 'Gilson', 'Rogerio')
print(f'A lista nomes contem {len(nomes)} pessoas')
print(f'Os primeiros 5 nomes são: {nomes[:5]}')
print(f'Os ultimos 4 nomes são: {nomes[-4:]}')
print(f'Os nomes em ordem alfabetica: {sorted(nomes)}')
print(f'O nome "Carol" está na posição: {nomes.index("Carol")}')