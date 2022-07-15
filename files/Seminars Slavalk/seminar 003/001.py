# найти строку в списке

col = ['g123', '123', 123, '123', '345', 'b123']
n_find = '123'

def f1(col, n_find):
    count = 0
    result = -1
    for i in range(len(col)):
            if col[i] == n_find:
                count += 1
                if count == 2:
                    result = i
    print('[{}]'.format(result))

f1(col, n_find)


# найти внутри элемента
def f2(col, n_find):
    result = False
    for i in range(len(col)):
        temp = str(col[i])
        #  result = temp.find('123')
        result = n_find in temp
    print(result)

f2(col, n_find)


# найти внутри элемента
def f3(col, n_find):
    result = False
    for i in col:
        temp = str(i)
        result = n_find in temp
    print(result)

f3(col, n_find)


# еще одно решение похожей, но другой задачи:
print(n_find in col)
 



