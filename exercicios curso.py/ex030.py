#numero e par ou impar?
n=int(input('Digite um número: '))
if n%2 ==0:
    print("\033[1;34m"'O número {} é PAR'.format(n),"\033[0;0m")
else:
    print("\033[1;34m"'O número {} é IMPAR'.format(n),"\033[0;0m")
