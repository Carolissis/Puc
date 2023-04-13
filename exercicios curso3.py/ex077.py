lista = ('arvore', 'carol', 'oi', 'computador', 
         'academia', 'exercicio', 'dia', 'uva')

for p in lista:
    print(f'\nAs vogais da palavra {p.upper()} são:', end='')
    for letra in p:
        if letra.lower() in "aeiou":
            print(letra, end=" ")
