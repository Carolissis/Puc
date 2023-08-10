#Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno,
#imprima o número de alunos com média maior ou igual a 7.0

notas = []
soma = 0
for n in range(4):
    nota = float(input(f'{n+1}º nota: '))
    notas.append(nota)
    soma += nota 
media = soma / 4
print('Suas notas foram:')
for i, v in enumerate(notas):
    print(f'{i+1}º: {v}')
print(f'Sua média foi: {media:.2}')
if media >= 7:
    print('APROVADO')
else:
    print('REPROVADO')