# Калькулятор от коллег

def Calc(arg_one, arg_two, operation):
	if operation == '+':
		return arg_one + arg_two
	if operation == '-':
		return arg_one - arg_two
	if operation == '*':
		return arg_one * arg_two
	if operation == '/':
		return arg_one / arg_two


status = True
while status != False:
	arg_one = float(input())
	operation = input()
	arg_two = float(input())
	result = Calc(arg_one, arg_two, operation)
	print(round(result))

	status = input('Введите "q", чтобы выйти из программы.')
	if status == 'q' or status == 'quit':
		status = False
