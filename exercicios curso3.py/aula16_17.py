#TUPLAS ()

def tupla():
     #  São imutaveis , podem obter itens str e int/float

    lanche = ('Hamburguer' , 'Suco', 'Pizza', 'Pudim')
    print(lanche[1])        # Mostra o segundo item da tupla 
    print(lanche[0:2])      # Começa no item zero  e termina antes do segundo 
    print(lanche[1:])       # Começa no segundo item e vai ate o final 
    print(lanche[0::2])     # Começa no zero, vai ate o final, printa de 2 em 2 

    print(sorted(lanche))   # Organiza a tupla 
    #del(lanche)              Apaga a tupla 
    len(lanche)             # Conta quantos elementos tem R:4

    for c in range(0,len(lanche)):
        print(lanche[c])

    a = (2,5,4)
    b = (5,8,1,2)
    c = a + b               # Soma a e b R: (2,5,4,5,8,1,2)
    
    print(len(c))           # Conta quantos elementos 
    print(c.count(5))       # Quantas vezes aparece o número 5 dento da tupla c
    print(c.index(5))       # Mostra a posição do número 5 R: 1 (mostra o primeiro)
    print(c.index(5, 2))       # Mostra em que posição está o número 5 a partir do item 2 R:37
     
# LISTAS [ ]

def lista():
    # Sao mutaveis 

    lista = ['Carol', 'Leo', 'Cadu']
    
    lista[2] = ('Rica')                 # Troca Cadu por rica 
    lista.append('Cadu')                # Vai adicionar Cadu a lista
    lista.issert(0, 'Dani')             # Vai add Dani na posicao 0 

    del lista[1]                        # Deleta o item da posicao 1
    lista.pop(3)                        # Deleta o ultimo, a nao ser que defina 
    lista.remove('Leo')                 # Deleta o item pelo nome ou valor dado a ele 
    # Apos deletar, a lista se refaz, numero dnd 

    valores = list(range(4,11))         # Faz valores virar uma lista de 4 a 10
    valor = [8,2,5,4,9,3,0]
    valores.sort()                      # Organiza em ordem a 
    valores.sort(reverse=True)          # Coloca de traz para frente 
    len(valores)                        # Conta quantos itens 