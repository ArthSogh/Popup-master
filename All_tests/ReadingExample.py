#read data from a txt file

file = open('reading_test.txt','r')
read = file.readlines()
lines = read.__len__()

cleaning_list = []
cleaning_list2 = []

for line in read:
    cleaning_list.append(line.strip())

"""for line in read:
    if line[-1] == '\n':
        cleaning_list.append(line[:-1])
    else:
        cleaning_list.append(line)"""

for line in cleaning_list:
    print(line)
    print(line.find("'"))
    if line.find(',') != -1:
        #cleaning_list.remove(line[line.find(',')])
        cleaning_list2.append(line)
        # cleaning_list2.append(line[:(line.find('5'))])
    else:
        cleaning_list2.append(line)

print(read)
print(cleaning_list)
print(cleaning_list2)