print('-'*5)
print(' CPF')
print('-'*5)

CPF = []

print('Digite o numero do seu CPF')
cpf = input(' ')

for c in range(11):
    CPF.append(int(cpf[c]))

soma = 0 
for c in range(9):
    soma+= CPF[c]*(10-c)

pdv= (soma*10)/11
if CPF[10] == pdv:
    print('Correto')
else:
    print('Nao verificado')