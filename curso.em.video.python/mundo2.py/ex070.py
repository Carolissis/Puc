print('\033[33mLISTA DE PRODUTOS\033[m')

total = quant = vmenor= totmil = 0
nmenor = ''

while True: 
    nome = str(input('Qual é o nome do produto? '))
    valor = float(input('Qual o valor do produto? '))

    total += valor
    quant +=1
    
    if quant == 1:
        vmenor = valor
        nmenor = nome
    else:
        if valor< vmenor:
            vmenor = valor
            nmenor = nome
    
    if valor < vmenor:
       vmenor = valor 
       nmenor = nome 

    if valor > 1000:
        totmil+= 1

    print('Deseja adicionar mais algum item? \n[1]SIM\n[2]NÃO')
    x = int(input('R: '))

    if x == 2:
        print(f'O total da compra é {total:.2f}')
        print(f'{totmil} produtos custam mais de R$1000,00 ')
        print(f'O produto mais barato foi {nmenor}')
        break 