#soma de um numero ate outro
s = 0
count = 0 
for n in range(1, 501, 2):
    if n %3 == 0:
        s = s + n 
        count = count + 1 
print('A soma de todos os valores solicitados é {}\nForam {} numeros'.format(s,count))
 