#Calcular aumento de salario
s= float(input('Qual o seu salário? R$'))
a= float(s+(s*15/100))
print('Seu salário de R${:.2f},com 15% de aumento, ficará R${:.2f}'.format(s,a))