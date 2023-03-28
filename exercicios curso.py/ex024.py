#crie um programa que leia o nome de uma cidade e diga se ela comeca ou nao com "santo"
cid= str(input('Digite o nome da cidade: ')).strip()
#print('Santo' in cid )
print(cid[:5].upper() == 'SANTO')
#colocar upper (ou lower) para dar true or false independente da forma que o usuario escrever 