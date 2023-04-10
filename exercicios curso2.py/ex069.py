print('\033[36m-='*8)
print('CADASTROS')
print('-='*8 , '\033[m')

maiores = homens = mulheres = cad = 0

while True: 
    idade = int(input('\033[32mQual a sua idade? '))
    sexo = str(input('Qual seu sexo [M/F]?\033[m ')).lower().strip()
    cad +=1
    if sexo in 'm':
        homens +=1
    
    if idade >= 18:
        maiores +=1 
    
    if sexo in 'f':
        if idade >= 20:
            mulheres +=1 
    
    print('Deseja continuar? \n[1]SIM\n[2]NÃO')
    resposta = int(input('R: '))

    if resposta == 2:
        print('\033[31mPROGRAMA ENCERRADO\033[m')
        print(f'\033[33m{cad} pessoas foram cadastradas')
        print(f'{maiores} pessoas tem 18 anos ou mais')
        print(f'{homens} homens foram cadastrados')
        print(f'{mulheres} mulheres cadastradas com 20 anos ou mais\033[m18')
        break
