# найти количесато вхождений в строке:
    
n = 'Урок 1: Общий рекрутмент: процесс отбора кандидатов глазами рекрутера'
m = 'Урок Общий рекрутментb: процессb отбора   рекрутера,'


a = n.split(' ')
b = m.split(' ')

def f(a, b):
    counter = 0
    text = ''
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                a[i] = a[i].upper()
                counter += 1
                text += ' ' + a[i]
    print(* a)
    print( '\nВсего ', counter, ' совпадения: ', text)

        
f(a, b)

