#Descobrir se a frase é um palíndromo

frase = str(input('Digite uma frase: ')).strip().upper()    #pede a frase ao usuario, tira os espacos (strip) e deixa em maiuscula(upper)

palavras = frase.split()    #split = separar a frase em palavras 
junto = ''.join(palavras)   #tira os espacos entre as palavras 
inverso = ''
for letra in range (len(junto)-1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Sua palavra é um palindromo!')
    print('{}, {}'.format(junto,inverso))
else:
    print('Sua palavra NÃO é um palindromo')
    print('{}, {}'.format(junto, inverso))
