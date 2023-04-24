N1= int(input("Prova 1: "))
N2= int(input("Prova 2: "))
N3= int(input("Prova 3: "))
#NF= Nota Final sem a P4
NF= (N1 + N2 + N3)/4
P4= (7- NF)*4  
print("Você precisa de {} na Prova 4 :)".format(P4))
N4= int(input("Prova 4: "))
#NF2= Nota Final
NF2= (N1+N2+N3+N4)/4
if NF2 >= 7:
    print("Aprovado ;)")
else:
    print("Reprovado :(")