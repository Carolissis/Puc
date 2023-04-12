# Solicitar ao usuário duas datas e calcular a quantidade de dias entre elas (levar em
# consideração os anos bissextos).

from datetime import date

data1_str = input("Digite a primeira data (DD/MM/AAAA): ")
data2_str = input("Digite a segunda data (DD/MM/AAAA): ")

data1 = date(int(data1_str[6:]), int(data1_str[3:5]), int(data1_str[:2]))
data2 = date(int(data2_str[6:]), int(data2_str[3:5]), int(data2_str[:2]))

dias = abs((data2 - data1).days)

print("A quantidade de dias entre as duas datas é:", dias)
 