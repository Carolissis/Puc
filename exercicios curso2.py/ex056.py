#Ler o  nome, idade e sexo de quatro pessoas
#indicar a media de idade, qual a idade do homem mais velho e seu nome
#falar quantas mulheres tem menos de 20 anos

media = 0
homem_maior = 0
homem = ''
idade_mulheres = 0

for p in range (1, 5):
    print('---- {} PESSOA ----'.format(p))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = int(input('Sexo [M(1)/F(2)]: '))
    media += idade 
    if sexo == 2:
        if idade < 20:
            idade_mulheres +=1
    if sexo == 1:
        homem_maior = p 
        homem = nome
    if idade > homem_maior:
        homem_maior = idade 
        homem = nome

print('A média das idades é {:.0f} anos'.format(media/4))
print('O homem mais velho tem {} anos e seu nome é {}'.format(homem_maior, homem))
print('Nesse grupo tem {} mulher(es) com menos de 20 anos'.format(idade_mulheres))


