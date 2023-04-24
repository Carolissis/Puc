#Caixa eletronico 

valor = int(input('Digite um valor: '))

qc = qv = qd = qu = 0

while True: 
    if valor >= 50:
        qc +=1
        valor -= 50
    elif valor >= 20:
        qv +=1
        valor -= 20 
    elif valor >= 10:
        qd +=1
        valor -= 10
    elif valor >=1:
        qu +=1
        valor -=1
    else:
        break 

print(f'Serão entregues:\n{qc} notas de R$50,00\n{qv} notas de R$20,00\n{qd} notas de R$10,00\n{qu} notas de R$1,00')
