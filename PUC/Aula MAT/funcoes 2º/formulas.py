import math

def bhaskara(a, b, c):
    delta = b ** 2 - 4 * a * c

    if delta < 0:
        return None
    elif delta == 0:
        x1 = -b / (2 * a)
        return x1, x1
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return x1, x2

a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))

raizes = bhaskara(a, b, c)

if raizes is None:
    print("A equação não possui raízes reais.")
else:
    x1, x2 = raizes
    print(f"Raízes da equação: x1 = {x1} e x2 = {x2}")

def calcula_vertice(a, b, c):
    # Calcular o valor de h (coordenada x do vértice)
    h = -b / (2 * a)

    # Calcular o valor de k (coordenada y do vértice)
    k = a * h**2 + b * h + c

    # Retornar o vértice como uma tupla (h, k)
    return (h, k)

# Exemplo de uso da função
a = 3
b = -1
c = -2
vertice = calcula_vertice(a, b, c)
print(f"O vértice da função quadrática é: {vertice}")

