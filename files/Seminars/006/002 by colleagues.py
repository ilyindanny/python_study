
# Альтернативный вариант от товарища.
# С моим примером не пашет.


#string = '245+34-16/4/2+(5-3*2-8/2)*2+56*34+16/4'
string = '-21*(2*(21+32))-(22-2)-(-100)'



def calculationInScope(scopeList):
    openScopeIndex = scopeList.index('(') + 1
    closeScopeIndex = scopeList.index(')')
    onlyScope = scopeList[openScopeIndex:closeScopeIndex]
    evalAll(onlyScope)
    scopeList[openScopeIndex - 1] = onlyScope[0]
    del scopeList[openScopeIndex:closeScopeIndex + 1]


def evalAll(currentList):
    while '(' in currentList:
        calculationInScope(currentList)
        break
    while '/' in currentList:
        calculate(currentList, '/')
    while '*' in currentList:
        calculate(currentList, '*')
    while '-' in currentList:
        calculate(currentList, '-')
    while '+' in currentList:
        calculate(currentList, '+')


def getResult(first, sec, symbol):
    
        if '*' in symbol:
            return first * sec
        elif '/' in symbol:
            return first / sec
        elif '+' in symbol:
            return first + sec
        elif '-' in symbol:
            return first - sec


def calculate(myList, symbol):
    indexSymbol = myList.index(symbol)
    first = myList[indexSymbol - 1]
    second = myList[indexSymbol + 1]
    myList.pop(indexSymbol)
    myList.pop(indexSymbol)
    myList[indexSymbol - 1] = getResult(first, second, symbol)


firstDigit = string[0]
tempDigit = str(firstDigit)
newList = []
firstIndex = 0
string += ' '
for index in range(1, len(string)):
    if not string[index].isdigit() and string[index - 1].isdigit():
        lastIndex = index
        newList.append(int(string[firstIndex:lastIndex]))
    if not string[index].isdigit():
        newList.append(string[index])
        firstIndex = index + 1
newList = newList[:-1]
evalAll(newList)
print('Строка из файла: {}'.format(string))
print('Результат вычислений программы: {}'.format(newList[0]))
print('Результат вычисления функции eval: {}'.format(eval(string)))