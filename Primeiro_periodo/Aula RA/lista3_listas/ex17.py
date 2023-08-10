cont = ['Primeiro', 'Segundo', 'Terceiro', 'Quarto', 'Quinto']
atleta = []
salto = []
saltos = []
media = []
while True:
    print('='*30)
    nome = input('Nome do atleta: ').title()
    if nome.strip() == '':
        break
    atleta.append(nome)
    salto = []
    for s in cont:
        alt = float(input(f'{s} salto: '))
        salto.append(alt)
    saltos.append(salto)
for i,s in enumerate(saltos):
    soma = 0
    for s in saltos[i]:
        soma += s
    me = soma / 5
    media.append(me)
print('RESULTADOS:')
for i,a in enumerate(atleta):
    print('='*30)
    print(f'Atleta: {a}')
    print(f'Saltos:',end='' )
    for s in saltos[i]:
        print(f'{s}m -',end='')
    print()
    print(f'Média dos saltos: {media[i]:.1f}m')