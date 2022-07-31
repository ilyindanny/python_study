def write_into_file():
	res = '\
	functions\n'


def f1(x):
	print('Hello world!')


with open('fs', 'a') as file:
	file.write('# functions\n')
