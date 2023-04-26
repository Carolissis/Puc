# Criar um programa que lê as temperaturas médias de cada mês
# do ano e as armazena em uma lista. Usar um outro vetor para
# guardar e exibir, quando necessário, os nomes dos meses do ano.
# Calcular a média anual de temperatura, e informar quais meses
# ficaram acima desta média anual.

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

