def aumentar(n, t):
    mais = n * (t/100)
    aumento = n + mais
    return aumento

def diminuir(n, t):
    menos = n * (t/100)
    sub = n - menos
    return sub

def dobro(n):
    return n*2

def metade(n):
    return n / 2

def moeda(n, moeda = 'R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')