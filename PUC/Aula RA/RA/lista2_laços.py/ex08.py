# Elaborar um programa que receba um número em binário, e mostre o seu valor em
# decimal.

numero_binario = input("Digite um número binário: ")

lista_binaria = list(map(int, numero_binario))
x = len(lista_binaria)

num = 0
for c in range(x):
    num += lista_binaria[c]*(2**(x-c-1))
   
print(num)

