dia = int(input('Dia: '))
mes = int(input('Mes: '))
ano = int(input('Ano: '))
hora = int(input('Hora: '))
min = int(input('Minuto: '))
seg = int(input('Segundo: '))

print("Data e hora informada: {}/{}/{} {}:{}:{}".format(dia, mes, ano, hora, min, seg ))

print('Qual informção você deseja acrescetar?')
print('Dia [1]')
print('Mes [2]')
print('Ano [3]')
print('Hora [4]')
print('Minuto [5]')
print('Segundo [6]')
opcao = int(input('R: '))

ultdias = 31 if mes in [1, 3, 5, 7, 8 , 10, 12] else 30 if mes in [4, 6, 9, 11] else 29 if (ano%4 == 0 and ano%100 !=0) or ano%400 == 0 else 28 
if opcao == 1: 
    qdias = int(input('Quantos dias deseja acrescentar? '))
    while qdias > 0: 
        
        if dia < ultdias:
            dia += 1 
        else:
            dia = 1 
            if mes < 12:
                mes +=1 
            else: 
                mes = 1
                ano +=1 
        qdias -= 1

elif opcao == 2:
    qmes = int(input('Quantos meses deseja acrescentar? '))
    while qmes > 0:
        if mes < 12:
            mes +=1
        else:
            mes = 1
            ano +=1
        qmes -= 1

elif opcao == 3:
    qanos =(int(input('Quantos anos deseja acrescentar? ')))
    while qanos >0:
        ano += qanos 
        qanos-=1


elif opcao == 4: 
    qhoras = int(input('Quantas horas? '))
    while qhoras > 0:
        if hora < 23:
            hora+= 1
        else:
            hora = 0 
            hora+= 1
        qhoras-=1

elif opcao == 5:
    qmin = int(input('Quantos minutos deseja adicionar? '))
    while qmin >0:
        if min < 59:
            min+=1
        else:
            min = 0
            if hora < 23:
                hora+=1
            else:
                hora= 0
                if dia < ultdias:
                    dia+=1
                else:
                    dia = 1 
                    if mes <12:
                        mes+=1
                    else:
                        mes = 1
                        ano+=1

        qmin-=1

elif opcao == 6:
    qseg = int(input('Quantos segundos deseja adicionar? '))
    while qseg>0:
        if seg < 59:
            seg+=1 
        else:
            seg = 0
            if min < 59:
                min+=1
            else:
                min=0
                if hora < 23:
                    hora+=1
                else: 
                    hora= 0
                    if dia < ultdias:
                        dia+=1
                    else:
                        dia= 1
                        if mes <12:
                            mes+=1
                        else:
                            mes = 1
                            ano+=1
        qseg -=1

print('Data/hora infromada: {}/{}/{} {}:{}:{}'.format(dia, mes, ano, hora, min, seg))        

