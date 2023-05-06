def moeda(n, moeda = 'R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')