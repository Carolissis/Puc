ficha = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Deseja adicionar mais algum aluno? [S/N]')).lower().strip()
    if resp != 's':
        break
print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*35)
    perg = str(input('Deseja saber a nota de algum aluno? [S/N] ')).lower().strip()
    if perg == 's':
        qual = int(input('Qual aluno? '))
        print(f'As notas de {ficha[qual][0]} são {ficha[qual][1]}')
    else:
        break

# aluno = []
# turma = []
# notas = []
# media = []
# while True:
#     nome = str(input('Digite o nome do aluno: '))
#     for c in range(0,2):
#         n = float(input(f'Digite a nota {c+1}: '))
#         notas.append(n)
#     media = (notas[0] + notas[1]) / 2
#     aluno.append([nome, media])
#     turma.append(aluno[:])
#     aluno.clear()
#     resp = str(input('Deseja adicionar mais algum aluno? [S/N]')).lower().strip()
#     if resp != 's':
#         break
# print('-='*30)
# print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
# print('-'*26)
# for i, a in enumerate(turma):
#     print(f'{i:<4}{a[0]:<10}{a[1]:>8.1f}')
# while True:
#     perg = str(input('Deseja saber a nota de algum aluno? [S/N] ')).lower().strip()
#     if perg == 's':
#         qual = int(input('Qual aluno? '))
#         print(f'{notas[qual]}')
#     else:
#         break
