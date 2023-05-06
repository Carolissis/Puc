def media(notas):
    s = 0
    for n in notas:
        s += n
    med = s / len(notas)
    return med