num  = 40
osn = 16
letters = '0123456789ABCDEFGHIJKLMNO.P.QRSTYVWXYZ'
result = ''
while num > 0:
    result = letters[num % osn] + result
    num //= osn
print(result)
