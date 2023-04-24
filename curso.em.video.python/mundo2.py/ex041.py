#Nivel de natacao 

ano = int(input('Que ano você nasceu? '))
idade = 2023 - ano 
if idade <= 9 :
    print('O atleta tem {} anos \nClassificação: MIRIM'.format(idade))
elif idade > 9 and idade <= 14:
    print('O atleta tem {} anos \nClassificação: INFANTIL'.format(idade))
elif idade > 14 and idade <= 19:
     print('O atleta tem {} anos \nClassificação: JUNIOR'.format(idade))
elif idade > 19 and idade <= 25:
     print('O atleta tem {} anos \nClassificação: SÊNIOR'.format(idade))
else:
      print('O atleta tem {} anos \nClassificação: MASTER'.format(idade))