with open('Seminars Slavalk/seminar 004/001.txt', 'r') as file_data:
    data = file_data.readline()

def find_minn_maxx(coll):
    nums = list(coll.split())
    maxx = nums[0]
    minn = nums[0]
    
    for i in nums:
        if i > maxx: maxx = i
        if i < minn: minn = i
    result = str(minn) + ' ' + str(maxx)

with open('001.py', 'a') as file_data:
    file_data.write('\n', find_minn_maxx(data))