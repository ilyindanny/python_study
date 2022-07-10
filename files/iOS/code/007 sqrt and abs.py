# расстояние между двумя точками 2 D

# точка a:
x1 = 0
y1 = 0

#точка b:
x2 = -3
y2 = -4

a = abs(float(x2 - x1))
b = abs(float(y2 - y1))
c = (a ** 2 + b ** 2) ** 0.5

print('a {}, b {}, c {}'.format(a, b, round(c, 2)))
