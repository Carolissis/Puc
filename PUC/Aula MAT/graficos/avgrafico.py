import matplotlib.pyplot as plt
import numpy as np

a = float(input('Digite o a: '))
def f(x, a):
    y = a**x
    return y

eixox = np.arange(-10, 10, 0.1)
eixoy = []

for x in eixox:
    y = f(x,a)
    eixoy.append(y)

fig =  plt.figure(figsize=(7,7))

plt.plot(eixox, eixoy, label = 'f(x) = a**x', color = 'g')
plt.title(f'f(x) = {a}**x')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.show()