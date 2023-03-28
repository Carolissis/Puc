#Quebrando um número
import math
x= float(input('Digite um valor: '))
#print('O valor digitado foi{} e a sua porção inteira é {:.0f}'.format(x,x))
print('O valor digitado foi{} e sua porção inteira é {}'.format(x, math.trunc(x)))