def escreva(pal):
    tam = len(pal)
    print('~'* (tam+2))
    print(f' {pal}')
    print('~'* (tam+2))


#Principal
pal = str(input('Digite uma palavra: '))
escreva(pal)