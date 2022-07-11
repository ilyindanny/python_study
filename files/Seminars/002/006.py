# дешифратор
alphabet_list = str(input("Введите пример: "))
str_a = ''
str_b = ''
t = 0
C = ''
for i in alphabet_list:
	if chr(ord(i)) == '+' or chr(ord(i)) == '-' or chr(ord(i)) == '*' or chr(ord(i)) == '/':
		C = chr(ord(i))
		t = 1
	elif t == 0:
		str_a = str_a + ''.join(chr(ord(i)))
	elif t == 1:
		str_b = str_b + ''.join(chr(ord(i)))
A = float(str_a)
B = float(str_b)

# тело калькулятора
if C == '/':
	if B == 0:
		print('На ноль делить нельзя')
	else:
		print(A / B)
if C == '+':
	print(A + B)
if C == '-':
	print(A - B)
if C == '*':
	print(A * B)
