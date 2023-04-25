# Cria um programa que peca ao usuario duas listas com 5 elementos cada,
# como resultado, criar uma terceira lista que intercala os elementos das duas listas

listas = list()
for l in range(2):
    lista = list()
    for n in range(5):
        dado = int(input(f'{l+1}° lista {n+1}° elemento: '))
        lista.append(dado)
    listas.append(lista[:])
print(listas)