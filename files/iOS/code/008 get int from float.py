
numm = 0.00000000978

n = numm
factor = 10
count = 0
while int(n) != n:
    n = numm
    n *= factor
    factor *=10
    count += 1
print(count)
