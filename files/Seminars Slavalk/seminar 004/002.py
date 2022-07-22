path = '002_text.txt'
data = []

with open(path, 'r') as file_text:
	for line in range(3):
		data.append(int(file_text.readline()))

print(data)

# D=b^2-4ac
d = data[1] ** 2 - 4 * data[0] * data[2]
print(d)

# x=((-b+ (d^ (1/2) )) / (2*a))
# x=((-b- (d^ (1/2) )) / (2*a))
x_1 = (-data[1] + d ** 0.5) / (2 * data[0])
x_2 = (-data[1] - d ** 0.5) / (2 * data[0])
print(x_1, x_2)

result = ''
with open(path, 'r') as file_text:
	for line in range(3):
		result += (file_text.readline())

result += f'x1 = {x_1}\nx2 = {x_2}'

with open(path, 'r+') as file_text:
	file_text.write(result)
