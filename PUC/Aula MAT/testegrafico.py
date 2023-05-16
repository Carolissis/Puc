import matplotlib.pyplot as plt
import numpy as np

#Função: 2x +1
# vetorX =[0,1,2,3,4,5]
# vetorY =[1,3,5,7,9,11]
#Criar figura 
# fig = plt.figure(figsize=(5,5))

# plt.plot(vetorX,vetorY, label = 'Função y= 2x + 1', color = 'g')

# plt.show()
def f(x):
    y = 2*x +1
    return y
vetorX = np.arange(-10,10,0.1)
vetorY = []
for x in vetorX:
    vetorY.append(f(x))
print(vetorX)