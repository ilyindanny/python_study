path = 'equation_text.txt'

with open(path, 'r') as my_file:
	data = my_file.read()

data = data.split()
print(data)

data = data[:-2]
print(data)

# a 1, b +12, c +7
data = [int(data[0][:-3]), int((data[1]) + (data[2])[:-1]), int(data[3] + data[4])]
print(data)

# D=b^2-4ac
d = data[1] ** 2 - 4 * data[0] * data[2]
print(d)

# x=((-b+ (d^ (1/2) )) / (2*a))
# x=((-b- (d^ (1/2) )) / (2*a))
x_1 = (-data[1] + d ** 0.5) / (2 * data[0])
x_2 = (-data[1] - d ** 0.5) / (2 * data[0])
print(x_1, x_2)
