ano = int(input('Que ano você nasceu? '))
idade = 2023 - ano 
if 2023 - ano == 18:
    print ('Você deve se alistar imediatamente!')
if 2023 - ano < 18:
    print('Quem nasceu em {} tem {} anos em 2023.'.format(ano, idade))
    print('Ainda faltam {} anos para o alistamento'.format(18 - idade))
    print('Seu alistamento será em {}'.format(2023+(18-idade)))
else:
    print('Quem nasceu em {} tem {} anos em 2023'.format(ano,idade))
    print('Você já deveria ter se alistado há {} anos'.format(idade-18))
    print('Seu alistamento foi em {}'.format(2023-(idade-18)))