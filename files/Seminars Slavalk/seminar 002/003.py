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


n = 'Урок 1: Общий рекрутмент: процесс отбора кандидатов глазами рекрутера'
m = 'Урок Общий рекрутментb: процессb отбора   рекрутера,'


a = n.split(' ')
b = m.split(' ')

def f(a, b):
    counter = 0
    text = ''
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                a[i] = a[i].upper()
                counter += 1
                text += ' ' + a[i]
        
    
    return a, ' всего ', counter, ' совпадения: ', text
    
    
    
        
print(*f(a, b))     



