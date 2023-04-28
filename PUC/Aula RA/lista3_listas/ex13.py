#Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto,
#calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas
#ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . )

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho',
         'Agosto','Setembro','Outubro', 'Novembro', 'Dezembro']

temperatura = list()
soma = 0
for t in range(12):
    temp = float(input(f'Temperatura média de {meses[t]}: '))
    temperatura.append(temp)
    soma += temp

media = soma / 12
mai = list()
for t in range(12):
    if temperatura[t] > media:
        mai.append(t)

print(f'A temperatura anual média é de {media:.2f} e os meses que estão acima dessa média são:')
for m in mai:
    print(meses[m])