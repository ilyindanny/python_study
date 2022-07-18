import json

a = int (input('input: '))

def num_row(x):
    x = list(range(-x, x+1))
    return x

data_result = num_row(a)

print(data_result)


with open('data.json', 'w', encoding = 'utf-8') as file:
    file.write(json.dumps(data_result, ensure_ascii = False))

print('json loaded')


with open('data.txt', 'w') as file:
    file.write(str(data_result))

print("txt loaded")

