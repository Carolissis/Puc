lista = []
consoantes = []
vogais = ['a', 'e', 'i', 'o', 'u']
palavra = str(input('Digite uma palavra: ')).lower()
for l in palavra:
    lista.append(l)
for l in lista:
    if l not in vogais:
        consoantes.append(l)
print(f'A palavra {palavra} tem {len(consoantes)} consoantes')