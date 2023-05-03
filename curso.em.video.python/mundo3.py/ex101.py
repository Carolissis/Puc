def lin():
    print('-'*18)

def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        lin()
        return (f'Com {idade} anos: VOTO NEGADO')
    elif 16 <= idade < 18 or idade > 65:
        lin()
        return (f'Com {idade} anos: VOTO OPCIONAL')
    else:
        lin()
        return (f'Com {idade} anos: VOTO OBRIGATORIO')

ano = int(input('Que ano você nasceu? '))
print(voto(ano))