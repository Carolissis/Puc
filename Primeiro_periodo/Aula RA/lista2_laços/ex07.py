# Elaborar um programa que solicita várias palavras ao usuário, sendo que o critério de
# parada é digitar uma palavra vazia. Contar e exibir quantas letras A existem neste
# conjunto de palavras.
contator = 0

palavra= input('Digite uma palavra: ')

while palavra != '':
    contator+=palavra.lower().count('a')
    palavra= input('Digite uma palavra: ')

print('O conjunto de palavras contem {} letras A'.format(contator))