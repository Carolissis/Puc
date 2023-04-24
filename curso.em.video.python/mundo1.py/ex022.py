#crie um prograama q leia o nome completo de uma pessoa e print o nome com todas as letras maiusculas, 
#todas minusculas,quntas letras tem(sem considerar espacos), quantas letras tem o primeiro nome
nome= str(input('Digite seu nome complreto: ')).strip()
def meuteste(): 
    nupper= nome.upper()
    print('Seu nome maiusculo é: {}'.format(nupper))
    nlower= nome.lower()
    print('Seu nome em letras minusculas é: {}'.format(nlower))
    num= len(nome)
    print('Quantas letras tem seu nome: {}'.format(num))
    div= nome.split()
    pri= len(div[0])
    print('Seu primeiro nome tem {} letras'.format(pri))
print('Analisando seu nome: ')
print('Seu nome em maiusculas é {}'.format(nome.upper()))
print('Seu nome em minusculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
print('seu primeiro nome tem {} letras'.format(len(nome[0])))