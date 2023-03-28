#Medir Hipotenusa
import math
x= float(input('Qual a medida do cateto oposto: '))
y= float(input('Qual a medida do cateto adjacente: '))
#hip=(x**2+y**2)**(1/2)
#print('A hipotenusa vai medir {:.2f}'.format(hip))
hi= math.hypot(x, y)
print('A hipotenusa vai medir {:.2f}'.format(hi))