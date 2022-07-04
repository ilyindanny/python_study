print ("Hallo world!")


 
count = 3
from array import *
days = array('i', [2, 3])
while count < 29:
    count = count + 3
    days.append(count)
    count = count + 1
    days.append(count)
for i in days:
    print (i)