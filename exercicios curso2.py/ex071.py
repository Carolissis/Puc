print('\033[35mCAIXA ELETRONICO')
print('~'*17, '\033[m')

print('Quantos reais você deseja sacar?')
valor = int(input('R$ '))

qc = qv = qd = qu = novovalor = 0
#quant cinquenta, vinte, dez, um

while True:
    if valor >= 50:
        qc = int(valor / 50)
        print(f'{qc} notas de R$50,00')
        novovalor = valor % 50 
            
        if novovalor >= 20:
            qv = int(novovalor / 20)
            print(f'{qv} notas de R$20,00')
            novovalor = novovalor % 20

            if novovalor >= 10:
                qd = int (novovalor / 10 )
                print(f'{qd} notas de R$10,00')
                novovalor = novovalor % 10 

                if novovalor >= 1:
                    qu = int (novovalor)
                    print(f'{qu} notas de R$1,00')
            
            elif novovalor >= 1:
                    qu = int (novovalor)
                    print(f'{qu} notas de R$1,00')

        elif novovalor >= 10:
                qd = int(novovalor)
                print(f'{qd} notas de R$10,00')
                novovalor = novovalor % 10

                if novovalor >= 1:
                    qu = int (novovalor)
                    print(f'{qu} notas de R$1,00')
        elif novovalor >= 1:
                    qu =  int (novovalor)
                    print(f'{qu} notas de R$1,00')        
    
    elif valor < 50 and  valor >= 20:
            qv = int (valor/20)
            print(f'{qv:.0f} notas de R$20,00')
            novovalor = valor % 20

            if novovalor >= 10:
                 qd = int (novovalor / 10 )
                 print(f'{qd} notas de R$10,00')
                 novovalor = novovalor % 10 
                 
                 if novovalor >= 1:
                    qu = int (novovalor)
                    print(f'{qu} notas de R$1,00')  
            
            elif novovalor >= 1:
                    qu =int (novovalor)
                    print(f'{qu} notas de R$1,00')    
    
    elif valor < 20 and valor >= 10:
            qd = int(valor/10)
            print(f'{qd} notas de R$10,00')
            novovalor = valor % 10 

            if novovalor >= 1:
                qu = int (novovalor)
                print(f'{qu} notas de R$1,00')              
    
    elif valor < 10 and valor  >= 1:
                qu = valor
                print(f'{qu} notas de R$1,00')         

    break        