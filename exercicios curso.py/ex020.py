#sorteando uma ordem na lista 
import random
n1= str(input('Chose a name: '))
n2= str(input('Chose another name: '))
n3= str(input('Chose another name: '))
n4= str(input('Chose another name: '))
lista =[n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem de apresentacao sera ')
print(lista)