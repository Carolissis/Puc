#Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor
#PAR e os números IMPARES no vetor impar. Imprima os três vetores.
inte = []
par = []
imp = []
for c in range(20):
    num = int(input(f'{c+1}º número: '))
    inte.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        imp.append(num)
inte.sort()
par.sort()
imp.sort()
print(f'Os números digitados fora: {inte}\n    Pares: {par}\n   Impares: {imp}')