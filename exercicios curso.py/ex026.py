#faca um programa que peca uma frase e diga quantas vezes aparece a letra A, em que posicao ela aparece 
#pela primeira vez, em que posicao ela aparece pela ultima vez
frase= str(input('Digite uma frase: ')).lower().strip()
print('A letra A aparece {} vezes na frase.'.format(frase.count('a')))
print('a letra A aparece a primeira vez na posição {}'.format(frase.find('a')+1))
print('A ultima letra A apareceu na posição {}'.format(frase.rfind('a')+1))