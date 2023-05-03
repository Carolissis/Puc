# AULA 20

def lin():
    print('-'*20)
# lin()
# print('Hello world')
# lin()

def mensagem(msg):
    print('-'*20)
    print(msg)
    print('-'*20)

# mensagem('Ola Carol')

def soma(a, b):
    s = a + b 
    print(f'A soma de {a} + {b} = {s}')


#Programa principal
# soma(a = 4, b = 5)
# soma(a = 2, b = 3)

def contador(* num):
    tam = len(num)
    print(f'Recebi os valores {num} e sao ao todo {tam} números')

#Programa principal
# contador(2,1,7)
# contador(1,2)
# contador(2,5,6,7)

def dobra(lst):
    pos = 0 
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

# valores = [5,7,8,12,3]
# dobra(valores)
# print(valores)

def soma(* valores):
    s = 0
    for num in valores:
        s+= num
    print(f'Somando os valores {valores} temos {s}')

soma(5, 2)
soma(1,4,5)

# AULA 21

def soma(a=0, b=0, c=0):
    s = a + b + c
    return s

r1 = soma(1,12,3)
r2 = soma(5,7)
r3 = soma(9)

print(f'Os resultados das somas foram {r1}, {r2}, {r3}')

def fatorial(num=1):
    f = 1
    for c in range(num,0,-1):
        f *= c
    return f
    
f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os fatoriais são {f1}, {f2}, {f3}')