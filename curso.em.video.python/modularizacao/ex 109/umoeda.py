def aumentar(n, t, format = False):
    mais = n * (t/100)
    aumento = n + mais
    return aumento if format is False else moeda(aumento)

def diminuir(n, t, format = False):
    menos = n * (t/100)
    sub = n - menos
    return sub if format is False else moeda(sub)

def dobro(n, format = False):
    dob = n*2
    return dob if format is False else moeda(dob)

def metade(n , format = False):
    met = n / 2
    return met if format is False else moeda(met)

def moeda(n, moeda = 'R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')