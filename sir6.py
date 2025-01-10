# file = open('./status.txt')  # relative path   os module, wd +join
# content = file.read()
# content = file.readlines()
# file.close()

# print(content)

database101 = []
with open('./status.txt') as file:
    content = file.readlines()
    print(content[1].strip())
    print('test')
    for each in content:
        updated = each.strip().split(',')
        database101.append(updated)

print(database101)
print(database101[1][2])
print(database101[1:])
# # sum_ = 0
# # for each in database101[1:]:
# #     sum_ += int(each[1])
# # avg = sum_//len(database101[1:])
# # print(avg)

# with open('sample.txt', 'w') as file:
#     file.write('sandip\n')
#     file.write(str(101))