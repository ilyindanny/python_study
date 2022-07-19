import json

x = 3

def num_row(x):
    x = list(range(-x, x+1))
    return x

data_result = num_row(x)

print(data_result)


with open('data.json', 'w', encoding = 'utf-8') as my_file:
    my_file.write(json.dumps(data_result, ensure_ascii = False))

print('json loaded')


with open('data.txt', 'w') as my_file:
    my_file.write(str(data_result))

print("txt loaded")

