input_number = int(input('Enter number: '))
number_to_letter = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in range(2, 37):
        x = input_number
        result_number = ''
        while x > 0:
            result_number += number_to_letter[x % i]
            x //= i
        print('{0} в C/C с основанием {1} = {2}'.format(input_number, i, result_number[::-1]))
