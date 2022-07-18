

# поиск слов:


data = open('file.txt')
text_coll = data.read()
data.close()

# создать список с уеикальными словами и указантем количества использования каждого слова:

def literary_method(start_col):
    coll = list(start_col.lower().split())
    length = len(coll)
    result = []
    while length:
        count = 0
        index = 0
        n = coll[0]

        while index <= length - 1:
            if n == coll[index]:
                del coll[index]
                count += 1
                length -= 1
            else:
                index += 1
        result.append(count)
        result.append(n)

    return result



# сортировка по частоте испольщования:

def sort_result(coll):
    coll = coll[0: len(coll)]
    result = []
    length = len(coll)

    while length:
        max = 0
       
        for i in range(0, length - 1, 2):            
            if coll[i] > coll[max]:
                max = i
        result.append(coll[max])
        result.append(coll[max + 1])
        del coll[max + 1]
        del coll[max]
        length -= 2
    for i in range(0, len(result), 2):
        print(result[i], ' - ', result[i + 1])
        
    
        
        
        
        

sort_result(literary_method(text_coll))
