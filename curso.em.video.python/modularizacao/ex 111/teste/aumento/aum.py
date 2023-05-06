def aumentar(n, t, format = True):
    mais = n * (t/100)
    aumento = n + mais
    return aumento if format is False else moeda(aumento)

def moeda(n, moeda = 'R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')