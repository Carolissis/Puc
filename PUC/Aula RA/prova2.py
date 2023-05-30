def questao2():    
    liq = dict( )
    while True:
        perg = input("Deseja adicionar bebida?").lower()
        if perg in "n":
            break
        else:
            liq['tipo'] = str(input('Bebida: '))
            liq['litros'] = int(input('Litros: '))

    for i, v in enumerate(liq):
        for c, l in enumerate(liq):
            if i != c:
                if liq['tipo'][i] == liq['tipo'][c]:
                    liq['litros'][i] += liq['litros'][c]
                    del liq[c]

    print (liq)

def questao3():
    lista = ['oi', 'maicris', 'tudo bem?']
    dic = {}

    def convert(lista):
        for i, v in enumerate(lista):
            return dic[i] == lista[v]
        
    print(convert(lista))

