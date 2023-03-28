#Seno, cosseno e tanguente
import math
x= float(input("Digitr o ângulo que você deseja: "))
co= math.cos(math.radians(x))
se= math.sin(math.radians(x))
ta= math.tan(math.radians(x))
print('O ângulo {:.0f} tem o SENO de {:.2f}'.format(x, se))
print('O ângulo {:.0f} tem o COSSENO de {:.2f}'.format(x, co))
print('O ângulo {:.0f} tem a TANGENTE de {:.2f}'.format(x,ta))