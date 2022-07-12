a = 'В программировании есть довольно много крутых и полезных вещей'
b = 'много'


def func(a: str, b: str):
	counter = 0
	for i in range(len(a)):
		if b in a[i:i + len(b)]:
			counter += 1
	print(counter)


func(a, b)


print(a.count(b))