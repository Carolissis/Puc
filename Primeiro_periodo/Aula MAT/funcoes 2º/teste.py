from formulas import bhaskara
from formulas import vertice


a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))

raizes = bhaskara(a, b, c)

if raizes is None:
    print("A equação não possui raízes reais.")
else:
    x1, x2 = raizes
    print(f"Raízes da equação: x1 = {x1} e x2 = {x2:.0f}")

print(f'Ponto que corta o eixo y= (0;{c})')

vert = vertice(a, b, c)
print(f"O vértice da função quadrática é: {vert}")