# input_number = int(input('Enter number: '))
# number_to_letter = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# for i in range(2, 37):
#     x = input_number
#     result_number = ''
#     while x > 0:
#         result_number += number_to_letter[x % i]
#         x //= i
#     print('{0} в C/C с основанием {1} = {2}'.format(input_number,
#           i, result_number[::-1]))


num = 20
letter = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

osn = 16
x = num
result = ''
while x > 0:
    result += letter[x % osn]
    x //= osn
print('{0} в C/C с основанием {1} = {2}'.format(num, osn, result[::-1]))
