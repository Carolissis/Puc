# Fazer um matriz identidade

resp = int(input('Quantas linhas/ colunas: '))

m = []
final = []
sub = []
for l in range(resp):
    for c in range(resp):
        if c == l:
            m.append(1)
        else:
            m.append(0)
for c in m:
    sub.append(c)
    if len(sub) == resp:
        final.append(sub)
        sub = []
for d in final:
    print(d)