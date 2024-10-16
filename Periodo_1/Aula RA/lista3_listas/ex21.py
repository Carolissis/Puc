count = 0
nome = []
litro = []
mil  = []
preco = []
menor = []
while True:
    print(f'Veículo {count+1}')
    n = input('Nome(para parar: fim): ').strip().capitalize()
    if n == 'Fim':
        break
    else:
        nome.append(n)
        l = int(input('Km por litro: '))
        litro.append(l)
        count += 1
men = 0
for l in litro:
    qnt = float(1000/ l)
    mil.append(qnt)
    p = float(2.25 * qnt)
    preco.append(p)
print('-'*15)
print('RELATÓRIO FINAL')
print('-'*40)
for i, n in enumerate(nome):
    print(f'{i+1}-{n:<10}{"- ":>2}{litro[i]:<3}{"- ":>2}{mil[i]:<5.2f}{" Litros"}{"- R$":>4}{preco[1]}')
