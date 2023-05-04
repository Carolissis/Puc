def fatorial(n, show=False):
    """
    -> Calcule o fatorial de um número.
    :param n: o número a ser calculado
    :param show: (opcional) mostrar ou nao a conta
    : return: o valor do fatorial de um número n 
     """
    f = 1
    for c in range(n, 0, -1):
        if show:
           print(c, end='')
           if c > 1:
               print(' X ',end='')
           else:
               print(' = ',end='')
        f *= c
    return f 
       

# Programa principal
print('='*40)
print(fatorial(7, show=True))
