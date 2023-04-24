print('-'*5)
print(' CPF')
print('-'*5)

CPF = []

print('Digite o numero do seu CPF')
cpf = input(' ')

for c in range(11):
    CPF.append(int(cpf[c]))

soma = 0 
for c in range(0,9):
    soma+= CPF[c]*(10-c)

x = (soma*10)
resto = x%11 

if resto == CPF[9]:
    print('Verificado')
elif resto == 10:
    if CPF[9]== 0:
        print('Verificado')
else: 
    print('Nao verificado')
print('O resultado da divisão acima é {} e o resto é {}'.format(soma, resto))

soma2= 0
for i in range(0,9):
    soma2+= CPF[i]*(11-i)

y= (soma2*10)
resto2= y%11

if resto2 == CPF[10]:
    print('Verificado')
else:
    print('Não verificado')
print('O resultado da divisão acima é {} e o resto é {}'.format(soma2, resto2))