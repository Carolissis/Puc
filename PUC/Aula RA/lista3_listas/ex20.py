# O salário de cada funcionário, juntamente com o valor do abono (20%);
# O número total de funcionário processados;
# O valor total a ser gasto com o pagamento do abono;
# O número de funcionário que receberá o valor mínimo de 100 reais;
# O maior valor pago como abono; A tela abaixo é um exemplo de execução do programa, apenas para fins
# ilustrativos. Os valores podem mudar a cada execução do programa

print('Projeção de Gastos com Abono')
print('='*28)

salario = []
abono = []
cont = 0
min = 0
while True:
    sal = int(input(f'{cont+1}º Salário: '))
    if sal != 0:
        salario.append(sal)
        abn = int(sal * 0.20)
        if abn >= 100:
            abono.append(abn)
        else:
            a = 100
            abono.append(a)
            min += 1
        cont +=1
    else:
        break
soma = 0
for a in abono:
    soma += a

print('{:<10}{:>10}'.format('Salário', '- Abono'))
for i, s in enumerate(salario):
    print(f'{"R$"}{s:<10.2f}{"- R$":<2}{abono[i]:.2f}')
print('='*28)
print(f'• Foram processado {cont} colaboradores')
print(f'• Total gasto com abonos: R$ {soma:.2f}')
print(f'• Valor mínimo pago a {min} colaboradores')
print(f'• Maior valor de abono pago: R$ {max(abono)}')