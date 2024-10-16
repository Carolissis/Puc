# Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘| ‘. Esta função deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor mínimo igual a 1 e o valor máximo é 20. Se valores fora da faixa forem informados, eles devem ser modificados para valores dentro da faixa de forma elegante

def moldura(l, c):
    nl = l 
    nc = c
    print(f'{"+"}{"-"*nl}{"+"}')
    for c in range(1,nc+1):
        print(f'{"|"}{" "*nl}{"|"}')
    print(f'{"+"}{"-"*nl}{"+"}')

linha = 0
coluna = 0
while True:
    linha = int(input('Qual a largura (min 1, max 20): '))
    if 1 <= linha <= 20:
        break
    else: 
        print('Por favor digite um valor entre/ igual 1 e 20')
while True:
    coluna = int(input('Qual o comprimento (min 1, max 20): '))
    if 1 <= coluna <= 20:
        break
    else: 
        print('Por favor digite um valor entre/ igual 1 e 20')

moldura(linha, coluna)
