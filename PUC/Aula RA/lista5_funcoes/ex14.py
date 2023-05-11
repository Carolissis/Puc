from random import shuffle

def quadrado_perf():
    count = 0 
    while True:
        n = [1 ,2 ,3 
             ,4 ,5 ,6 
             ,7 ,8 ,9]
        shuffle(n)
        count +=1
        if n[0]+ n[1] + n[2] == n[0] + n[3]+ n[6] and n[1]+ n[4]+ n[7] == n[3]+ n[4]+ n[5] and n[2]+n[5]+n[8] == n[6]+ n[7]+ n[8]:
            for c in range(9):
                print(n[c], end=' ')
                if c == 2 or c == 5:
                    print()
            print()
            print(f'Foram {count} tentativas até o quadrado perfeito')
            break
quadrado_perf()                 
