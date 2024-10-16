lista = []
teste = [0] * 23

while True:
    num = int(input('Camisa do jogador [1-23] e [0 para encerrar]: ').strip())
    if num == 0:
        break
    elif 1 > num > 23:
        print('Número invalido')
    elif 1 <= num <= 23:
        lista.append(num)

print('\nRESULTADO')
print(f'Houve {len(lista)} votos')

org = list(set(lista))
org.sort()

melhorjog = 0
melhorvot = 0

print('_'*36)
print('{:<13}{:>5}{:>18}'.format('Jogador', 'Votos', 'Porcentagem'))
for c in range(23):
    qtd = lista.count(c+1)
    teste[c] = qtd
    if qtd > melhorvot:
        melhorvot = qtd
        melhorjog = c+1
melhorporc = 0
for c in org:

    perc = float('{:.1f}'.format(teste[c-1]/len(lista)*100))

    if perc > melhorporc:
        melhorporc = perc

    print('{:<13}{:>5}{:>17}%'.format(c, teste[c-1], perc))
print('⁻'*36)


bct = teste[(teste.index(max(teste))+1)]/len(lista)*100

try:
    print('O melhor jogador foi o número {}, com {} votos, correspondendo a {}% do total de votos'.format(melhorjog, melhorvot, melhorporc))

except ValueError:
    print('Houve empate entre os melhores jogadores. O campeão será verificado na próxima votação')
