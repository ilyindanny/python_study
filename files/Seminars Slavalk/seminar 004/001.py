# Seminars Slavalk/seminar 004/001.txt

with open('Seminars Slavalk/seminar 004/001.txt', 'r') as file_data:
    data = file_data.readline()


def find_minn_maxx(coll):
    nums = list(map(int, coll.split()))
    maxx = nums[0]
    minn = nums[0]
    
    for i in nums:
        if i > maxx:
            maxx = i
        if i < minn:
            minn = i
    return 'min = ' + str(minn) + ',  = ' + str(maxx)


result = find_minn_maxx(data)


# with open('001.py', 'a') as file_data:
# 	file_data.write('\n# {}\n\n'.format(result))

with open('Seminars Slavalk/seminar 004/001.txt', 'a') as file_data:
    file_data.write('\n# {}\n\n'.format(result))


