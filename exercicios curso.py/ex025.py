#crie um programa que leia o nome de uma pessoa e diga se ela tem SILVA no nome 
n= str(input('Digite seu Nome: ')).strip() 
x= "silva" in n.lower()
print('Seu nome tem silva? {}'.format(x))