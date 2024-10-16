# Elaborar um programa que receba o nome completo do usuário, e imprima apenas o
# primeiro e último nome.

print('\033[34m='*25)
print('Priemiro e ultimo nome')
print('='*25,'\033[m')


nome = str(input('Qual é o seu nome completo? '))

palavras = nome.split()
primeiro_nome = palavras[0].capitalize()
ultimo_nome = palavras[-1].capitalize()


print('\033[30;45mSeu primeiro nome é {} e o ultimo é {}\033[m'.format(primeiro_nome, ultimo_nome))