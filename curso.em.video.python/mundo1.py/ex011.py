#Pintura da parade
lar= float(input('Largura da parede: '))
alt= float(input('Altura da parde: '))
a= alt*lar
t= a*(1/2)
print('Sua parede tem a dimensão {:.2f}X{:.2f} e sua área é de {:.2f}m2.'.format(lar, alt, a))
print('Para pintar sua parede, você precisrá de {:.2f}L de tinta.'.format(t))