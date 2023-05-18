def teste4():
    B= {1,2,2,2,3,4,5,5}
    len(set(B))
    print(len(set(B)))
def teste6():
    A= {1,2,3}
    B= {3,2,1}
    #teste
    if A==B:
        print(True)
    else:
        print(False)
def teste7():
    C= {2,3,4}
    a= {4}
    b={2}
    c= {3}
    d= {2,3,4}
    e= {7}
    print(a.issubset(C))
    print(b.issubset(C))
    print(c.issubset(C))
    print(d.issubset(C)) 
    print(e.issubset(C))
def teste7_1():
    A = {1,2,3,4,5}
    print({1,2} in A) 
    print(1 in A)
    print(2 in A)
def teste7_2():
    A= {1,2,3,4,5}
    #print(∅ in A)
def teste8():
    A={1,2,3}
    C={1,2,3,4,5}
    D={5,3,4,2,1}
    print(A.issubset(C))
    print(D.issubset(C))
def teste9():
    A= {1,2,3,4,5}
    B= {4,5,6,7,8,9,10}
    #a)
    print(A.union(B))
    #b)
    print(A.intersection(B))
    #c)
    print(A.difference(B))
    #d)
    print(B.difference(A))
teste6()

