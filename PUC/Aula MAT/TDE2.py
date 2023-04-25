# Exercício extra sobre Médias:
# Implemente um programa que permita que o usuário calcule a média de suas notas. O usuário
# deverá escolher se o esquema de notas é por média aritmética ou ponderada. Após escolher o
# tipo, deverá ser perguntado a quantidade de notas (pesos quando necessário). O usuário
# informará as notas (pesos) e a média final deverá ser calculada.
# Ainda, deverá ter a opção de “calcular quanto falta para passar”. Assim, deverá ser informado a
# quantidade de notas e os respectivos valores menos um (deverá ser somente um faltante). O
# usuário também deverá informar a média necessária para aprovação. Por fim, o programa
# informa quanto deve ser essa nota faltante para atingir o resultado.

while True: 
    opcao = int(input('Fazer:\n[1]Média Aritmética\n[2]Média Ponderada\nR:'))
    if opcao == 1 or opcao == 2:
        break 

if opcao == 1:
    quantsp = int(input('Fazer média de qunatas provas?\nR: '))
    media   = float(input('Qual a média para ser aprovado?\nR: '))
    soma    = 0 
    for p in range(quantsp):
        nota = float(input(f'Digite a {p+1}º nota: '))
        soma += nota
    ma = soma / quantsp
    if ma >= media:
        print(f'Parabens! Você foi aprovado com média {ma:.2f}')
    else: 
        falta = (media - ma) * quantsp
        print(f'Falta {falta:.2f} para ser aprovado')

if opcao == 2:
    quantsp = int(input('Fazer média de quantas provas?\nR: '))
    media   = float(input('Qual a média para ser aprovado?\nR: '))
    p      = 0      # Peso
    soma    = 0     # Soma das notas com peso  
    for p in range(quantsp):
        nota = float(input(f'Valor da {p+1}º nota: '))
        peso = int(input(f'Peso da {p+1}º nota: '))
        p   += peso
        soma+= (nota * peso)
    mp = soma / peso
    if mp >= media:
        print(f'Parabens! Você foi aprovado com média {mp:.2f}')
    else: 
        falta = (media - mp) * quantsp
        print(f'Falta {falta:.2f} para ser aprovado')