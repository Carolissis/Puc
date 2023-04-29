marcas = ['Windows', 'Unix', 'Linux','Netware', 'Mac OS', 'Outro']
opc = []
cont = 0
votos = [0]*6
porcentagem = []

print('Qual o melhor Sistema Operacional para uso em servidores?')
for i,m in enumerate(marcas):
    print(f'{i+1}- {m}')
while True:
    opcao = int(input(f'Voto {cont+1}(0=FIm): '))
    if opcao == 0:
        break
    elif 1<= opcao <=6:
        opc.append(opcao)
        cont += 1
    else:
        print('Número inválido')
org = list(set(opc))
org.sort()

print('-'*35)
print('{:<20}{:>6}{:>6}'.format('Sistema Operacional','Votos','%'))
print('{:<20}{:>6}{:>9}'.format('-'*18,'-'*5,'-'*4))

maisvot = 0
melhor = 0
for c in range(6):
    qtd = opc.count(c+1)
    votos[c] = qtd
    if qtd > maisvot:
        maisvot = qtd
        melhor = c

melhorporc = 0
tot = len(opc)
for c in org:
    porc = votos[c-1]/tot*100
    porcentagem.append(porc)
    if porc > melhorporc:
        melhorporc = porc

for c in range(6):
    print(f'{marcas[c]:<20}{votos[c]:>6}{porcentagem[c]:>9.2f}')
print('-'*35)
print('{:<20}{:>6}'.format('Total', cont))
print()
print(f'O sistema mais votado foi {marcas[melhor]} com {maisvot} votos, equivalente a {melhorporc:.2f}% dos votos')