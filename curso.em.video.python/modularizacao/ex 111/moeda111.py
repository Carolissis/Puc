from teste.aumento import aum
from teste.desconto import des
from teste.dobro import dob
from teste.metade import met
from teste.moeda import moe


num = float(input('Digite um valor:\nR$'))
aume = int(input('Taxa de aumento: '))
desc = int(input('Taxa de desconto: '))
print(f'O valor {moe.moeda(num)} com um aumento de {aume}% é {aum.aumentar(num, aume, True)}')
print(f'O valor {moe.moeda(num)} com um desconto de {desc}% é {des.diminuir(num, desc, True)}')
print(f'O dobro de {moe.moeda(num)} é {dob.dobro(num, True)}')
print(f'A metade de {moe.moeda(num)} é {met.metade(num, True)}')