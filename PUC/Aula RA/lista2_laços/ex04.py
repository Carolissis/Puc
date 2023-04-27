# Peça 5 números ao usuário. Fazendo uso de laços, organize e mostre eles em ordem
# crescente.

numeros = []

for i in range(5):
    numero = float(input("Digite um número: "))
    numeros.append(numero)

numeros.sort()

print("Os números em ordem crescente são:", end=" ")

for numero in numeros:
    print(numero, end=" ")
