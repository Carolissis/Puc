print('-'*20)
print('Conversão de bases')
print('-'*20)

num = int(input('Digite um numero inteiro: '))
print('Escolha uma das bases:')
print('[1] converter para BINÁRIO')
print('[2] converter para OCTAL')
print('[3] converter para HEXADECIMAL')
x = int(input("Sua opção: "))

if x == 1: 
    print('{} convertido para binário é igual a {}'.format(num, bin(num)[2:]))
elif x == 2:
    print('{} convertido para octal é igual a {}'.format(num, oct(num)[2:]))
elif x == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção invalida, tente novamente.')