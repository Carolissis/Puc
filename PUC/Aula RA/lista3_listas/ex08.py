#Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor.
#Imprima a idade e a altura na ordem inversa a ordem lida

altura = []
nomes = []

for p in range(5):
    n = str(input('Nome: ')).title()
    nomes.append(n)
    altura.append(float(input('Altura: ')))
nomes.reverse()

altura.reverse()
for i, n in enumerate(nomes):
    print(f'{n} tem {altura[i]}cm de altura')
    