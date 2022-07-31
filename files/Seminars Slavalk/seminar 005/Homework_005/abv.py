# Напишите программу, удаляющую из текста все слова, содержащие "абв".

path = 'abv.txt'
with open(path) as file:
	start_string = file.read()

print(start_string)
word = 'абв'

result = list(filter(lambda i: word not in i, start_string.split()))
print(*result)

# Второй вариант решения:
result = [i for i in start_string.split() if word not in i]
print(*result)
