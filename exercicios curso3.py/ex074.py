from random import randint

a = randint(0,20)
b = randint(0,20)
c = randint(0,20)
d = randint(0,20) 
e = randint(0,20) 

num = (a, b, c, d, e)

print(f'Os números sorteados foram: {num}')
print(f'O menor número sorteado foi {min(num)}')
print(f'E o maior foi {max(num)}')