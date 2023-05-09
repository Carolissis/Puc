def contrario(num):
    num_str = str(num)
    num_inver = num_str[::-1]
    num_inver = int(num_inver)
    return num_inver

num = int(input('Digite um número: '))
print(contrario(num))