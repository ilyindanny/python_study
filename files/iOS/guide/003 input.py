

# возвращает только int:

a = [int(x) for x in input('Enter line: ').split() if x.isnumeric()]
print(a)

for i in a:
    print(type(i))
    
    
# возвращает int и str:
# принимает строку

a = [int(x) if x.isnumeric() else x for x in input('Enter line: ').split()]
print (a)

for i in a:
    print(type(i))


# возвращает int, float или str:

def f():
    col = list(input('Enter int, float or str: ').split())

    for i in range(len(col)):
        try:
            col[i] = int(col[i])
        except ValueError:
            try:
                col[i] = float(col[i])
            except ValueError:
                pass
    for i in col:
        print(type(i))

f()


# в одну строку. возвращает int, float или str:

b = list(int(x) if x.isdigit() else float(x) if x.count('.') == 1 else x for x in input ('Enter line: ').split())

for i in b:
        print(type(i))














