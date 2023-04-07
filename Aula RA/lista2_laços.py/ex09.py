# Elaborar um programa em Python que converta um número decimal em hexadecimal,
# fazendo uso do método de divisões sucessivas

numero_decimal = int(input("Digite um número decimal: "))
num_hexadecimal = ""

while numero_decimal > 0:
    resto = numero_decimal % 16
    if resto < 10:
        num_hexadecimal += str(resto)
    elif resto == 10:
        num_hexadecimal += "A"
    elif resto == 11:
        num_hexadecimal += "B"
    elif resto == 12:
        num_hexadecimal += "C"
    elif resto == 13:
        num_hexadecimal += "D"
    elif resto == 14:
        num_hexadecimal += "E"
    elif resto == 15:
        num_hexadecimal += "F"
    numero_decimal = numero_decimal // 16

num_hexadecimal = num_hexadecimal[::-1]

print("O número em hexadecimal é:", num_hexadecimal)


# def decimal_para_hexadecimal(decimal):
#     tabela_hexa = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
    
#     restos = []
    
#     while decimal > 0:
#         resto = decimal % 16
#         if resto >= 10:
#             resto = tabela_hexa[resto]
#         restos.append(resto)
#         decimal = decimal // 16
    
#     hexa = ''.join(map(str, restos[::-1]))
#     return hexa
