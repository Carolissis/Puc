opcao = 1
lista = [1, 2, 3, 4, 5]

num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))

while opcao !=5:
    print('[1] Somar\n[2] Multiplicar\n[3] Qual é maior\n[4] Novos números\n[5] Sair do programa')
    opcao = int(input('R: '))
    if opcao == 1: 
        print('A soma entre {} e {} é {}!'.format(num1, num2, (num1 + num2)))
    elif opcao == 2:
        print('A multipicacao entre {} e {} é {}!'.format(num1, num2, (num1*num2)))
    elif opcao == 3:
        if num1 > num2:
            print('Entres os números {} e {} o número {} é maior!'.format(num1, num2, num1))
        elif num1< num2: 
            print('Entres os números {} e {} o número {} é maior!'.format(num1, num2, num2))
        elif num1 == num2:
            print('Os valores são iguais')
    elif opcao == 4: 
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor: '))
        print('[1] Somar\n[2] Multiplicar\n[3] Qual é maior\n[4] Novos números\n[5] Sair do programa')
        opcao = int(input('R: '))
    elif opcao != lista:
        print('Opção invalidada.')
        print('[1] Somar\n[2] Multiplicar\n[3] Qual é maior\n[4] Novos números\n[5] Sair do programa')
        opcao = int(input('R: '))
print('Você saiu do programa. Até a proxima ;)')