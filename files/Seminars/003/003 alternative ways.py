a = [1,2,3,4,3]

def f(a):
    l = []
    m = []
    for i in a:
        if i in l and i not in m:
            m.append(i)
        l.append(i)
    print(set(l).difference(set(m)))

f(a)

def f2(a):
    
    m = []
    index = 0
    for i in a:
        if i in a[:index] and i not in m:
            m.append(i)
        index +=1
    print(set(a).difference(set(m)))

f2(a)