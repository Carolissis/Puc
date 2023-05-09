def posouneg(num):
    if num > 0:
        return 'P'
    elif num < 0:
        return 'N'
    
num = int(input('Digite um valor: '))
print(posouneg(num))