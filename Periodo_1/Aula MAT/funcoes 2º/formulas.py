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

def vertice(a, b, c):
    # Calcular o valor de h (coordenada x do vértice)
    h = -b / (2 * a)

    # Calcular o valor de k (coordenada y do vértice)
    k = a * h**2 + b * h + c

    # Retornar o vértice como uma tupla (h, k)
    return (h, k)


