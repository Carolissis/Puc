#media 

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1+n2)/2
print('Tirando {:.2f} e {:.2f}, a média do aluno é {:.2f}'.format(n1, n2, media))
if media >= 7:
    print('O aluno está APROVADO')
else:
    print('O aluno está REPROVADO')