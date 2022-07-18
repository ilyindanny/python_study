# поиск слов:


data = open('file.txt')
text_of_book = data.read()
data.close()


# создание массива без знаков препинания из текста:

def text_coll(start_str):
	temp_coll = ''
	for el in start_str:
		if el == '–' or el == ',' or el == '.' or el == '!' or el == '?' or el == '-' or el == ':' or el == ';' or el == '\'' or el == '"' or el == '«' or el == '»':
			continue
		else:
			temp_coll += el

	result = list(temp_coll.lower().split())

	return result


# создать список с уникальными словами и указанием количества использования каждого слова:

def literary_method(coll):
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


# сортировка по частоте использования:

def sort_result(coll):
	coll = coll[0: len(coll)]
	result = []
	length = len(coll)

	while length:
		max_index = 0

		for i in range(0, length - 1, 2):
			if coll[i] > coll[max_index]:
				max_index = i
		result.append(coll[max_index])
		result.append(coll[max_index + 1])
		del coll[max_index + 1]
		del coll[max_index]
		length -= 2
	for i in range(0, len(result), 2):
		print(result[i], ' - ', result[i + 1])


# получить список из букв без знаков препинания:
collection_from_book = text_coll(text_of_book)

# создать список с уникальными словами и количеством использования:
uniq_words = literary_method(collection_from_book)

# отсортировать и распечатать:
sort_result(uniq_words)
