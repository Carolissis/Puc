def moeda(n, moeda = 'R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')

def lin():
    print('-'*30)

def resumo(n, aum = 10, dec = 10):
# aumento
    mais = n * (aum/100)
    aumento = n + mais
# desconto
    menos = n * (dec/100)
    sub = n - menos
#dobro
    dob = n*2
# metade 
    met = n / 2

    lin()
    print('RESUMO DO VALOR'.center(30))
    lin()
    print(f'{"Preço analisado:":<16}{moeda(n):>13}')
    print(f'{"Dobro do preço:":<16}{moeda(dob):>13}')
    print(f'{"Metade do preço:":<16}{moeda(met):>13}')
    print(f'{aum}{" de aumento:":<14}{moeda(aumento):>13}')
    print(f'{dec}{" de redução:":<15}{moeda(sub):>13}')
    lin()