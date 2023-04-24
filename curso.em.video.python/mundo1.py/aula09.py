frase= 'Curso em Vídeo Python'
def teste01():
    #teste de corte 
        print(frase)
        #contar quantos caracteres 
        print(len(frase))
        #qual caracter pertence a tal lugar
        print(frase[9])
        #cortanto a palavra de 7 a 9 (cancela o 10)
        print(frase[7:10])
        # de 3 a 11 pulando de 2 em 2
        print(frase[3:12:2])
        #termina em 7
        print(frase[:7])
        #comeca em 6
        print(frase[6:])
        # comeca no 4, vai ate o final pulando de 3 em 3 
        print(frase[4::3])
def teste02():
    #quantas vezes parece x
    print(frase.count('o'))
    #quantas vezes entre x e y
    print(frase.count('o',0,6))
    #achar um caracter 
    print(frase.find('em'))
    #onde comceca a palavra
    print(frase.find('Curso'))
    print(frase.find('em'))
    print(frase.find('oi'))
    #true or false in Find
    print("oi"in frase)
    print('em'in frase)
def teste03():
#deixar Maiuscula, Minuscula, capitalizar, titulo
    print(frase.upper())
    print(frase.lower())
    print(frase.capitalize())
    print(frase.title())
def teste04():
     x= frase.split()
     print(x)
     print(x [2])
     print(x [2][3])
teste04()