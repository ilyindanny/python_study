import time

def current_milli_time():
    return round (time.time())

number = int(input("Size?"))
tmp = 1
array = []
for i in range ((number + 1) // 3):
    array.append(tmp * (current_milli_time() // 100))
    array.append((tmp * (current_milli_time() // 100)) // 3)
    array.append((tmp * (current_milli_time() // 100)) // 100)
print (array)