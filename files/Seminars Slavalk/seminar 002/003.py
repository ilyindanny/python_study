a1 = 'Ссылка на трансляцию появится здесь за 10 минут до начала вебинара.'
b2 = 'на трансляцию здесь за до'


def f(a, b):
	n = a[:].split(' ')
	m = b[:].split(' ')
	counter = 0
	for i in range(len(n)):
		for j in range(len(m)):
			if i == j:
				n[i] = n[i].upper()
				counter += 1

	return n, counter


print(f(a1, b2))
