n = soma = quant = 0 

while True:
    n = int(input('Digite um numero [999 para parar]: '))
    if n == 999:
        break
    quant += 1
    soma += n
print(f'Foram {quant} números e a soma engtre eles é {soma}')