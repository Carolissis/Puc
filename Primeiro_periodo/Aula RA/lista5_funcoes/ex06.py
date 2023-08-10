def hora(h, m):
    if h <= 12:
        return f'{h}:{m} A.M'
    elif h > 12:
        return f'{h-12}:{m} P.M'

hor = int(input('Digite a hora: '))
min = int(input('Digite o minuto: '))
print(hora(hor,min))