#Analisar a idade de sete pessoas, dizer quantas são de maior e quantas não 

anos = []
for c in range(1,8):
    print('Em que ano a {} pessoa nasceu?: '.format(c))
    ano = int(input(' '))
    anos.append(ano)

maiores = 0
menores = 0
for i in range(0,7):
    x = 2023 - anos[i]
    if x >= 18:
        maiores+=1
    else:
        menores+=1

print('Existem {} maiores e {} menores no grupo'.format(maiores, menores))

# from datetime import date
# atual = date.today().year
# totmaior = 0
# totmenor = 0
# for pess in range(1, 8):
#     nasc = int(input('Em que ano a {} pessoa nasceu?'.format(pess)))
#     idade = atual - nasc
#     if idade >= 21:
#         totmaior +=1
#     else:
#         totmenor +=1
