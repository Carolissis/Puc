# Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada
# de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados,
# faça:
# h. Encerre o programa com uma mensagem

lista = []
soma = 0
acima = 0
abaixo = 0 
count = 1

while True:
    num = float(input(f'Digite o valor da {count}º nota (-1 para parar)\nR: '))
    if num != -1:
        lista.append(num)
        count += 1
    elif num == -1:
        break
    

print(f'{len(lista)} números foram digitados')          # a. Mostre a quantidade de valores que foram lidos;

for n in lista:
    print(f'{n},',end='')                               # b. Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
print()

for n in lista: 
    print(n)                                            # c. Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;

for n in lista:
    soma+= n
print(f'A soma desses números é {soma}')                # d. Calcule e mostre a soma dos valores;

media = soma / len(lista)
print(f'A média é igual a {media}')                     # e. Calcule e mostre a média dos valores;

for n in lista:
    if n > media:
        acima += 1
    if n < 7:
        abaixo += 1
print(f'{acima} notas ficaram acima da média')          # f. Calcule e mostre a quantidade de valores acima da média calculada;
print(f'{abaixo} notas ficaram abaixo de 7')            # g. Calcule e mostre a quantidade de valores abaixo de sete;

if media >= 7:
    print(f'Parabens! Voce foi aprovado, sua média foi superior a 7!')
else:
    print(f'Voce reprovou, sua média foi menor que 7')