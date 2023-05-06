def diminuir(n, t, format = True):
    menos = n * (t/100)
    sub = n - menos
    return sub if format is False else moeda(sub)

def moeda(n, moeda = 'R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')