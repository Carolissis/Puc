def dobro(n, format = False):
    dob = n*2
    return dob if format is False else moeda(dob)

def moeda(n, moeda = 'R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')