#Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de
#13 anos possuem altura inferior à média de altura desses alunos

somaalt = 0
ida = []
alt = []
n_alunos = int(input('Quantos alunos? '))
for a in range(n_alunos):
    print(f'{a+1}º ALUNO')
    idade = int(input('Idade: '))
    ida.append(idade)
    altura = float(input('Altura: '))
    alt.append(altura)
    somaalt += altura
media = somaalt / n_alunos
soma = 0 
for i in range(n_alunos):
    if ida[i] > 13 and alt[i] < media:
        soma += 1

print(f'{soma} alunos tem mais de 13 anos e tem altura menor do que a média de {media:.2f}')