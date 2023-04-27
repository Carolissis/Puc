notas = []
soma = 0
for n in range(4):
    nota = float(input(f'{n+1}º nota: '))
    notas.append(nota)
    soma += nota
media = soma / 4 
print(f'Suas notas foram {notas} e sua media foi {media:.2f}')
if media >= 7:
    print('Aprovado')
else:
    print('Não foi aprovado')