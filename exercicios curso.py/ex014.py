#Celsius p Fahrenheit ou Fahrenheit para Celsius 
def teste01():
    #minha tentativa 
    x= int(input('De F para C (1) ou de C para F(2)? '))
    if x==1:
        f= float(input('Quantos Fahrenheits? '))
        c= float(5*((f-32)/9))
        print('{:.1f} Fahrenheit é igual a {:.0f} graus Celsius'.format(f,c))
    elif x==2:
        C= float(input('Quantos Celsius? '))
        F= float(C*1.8+32)
        print('{:.0f} graus Celsius são iguais a {:.1f} Fahrenheit'.format(C,F))
def teste02():
    #video aula 
    c=float(input('Informe a temperatura em C '))
    f= 9*c/5+32
    # ou f=9*5/c+32 (igual)
    print('A Temp de {:.1f}C corresponde a {:.1f}F!'.format(c,f))

teste02()
