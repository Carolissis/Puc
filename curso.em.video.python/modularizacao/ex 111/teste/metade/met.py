def metade(n , format = False):
    met = n / 2
    return met if format is False else moeda(met)

def moeda(n, moeda = 'R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')