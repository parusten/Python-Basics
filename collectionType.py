'''
single value: primitive: int, float, str, bool
data collection in single variable: array
data + behavior/method: object
'''

"""
Collection/Iterables:
1. Mutable
2. Data positioning/ order
3. Data retrieve: indexing for ordered one
"""
# # List : ordered mutable collection of data
# lstStudent = ["name1", "name2"]
# lstTeacher = ["name1", 12, lstStudent, 1.0, 12, True]
# print(len(lstTeacher))

# # for ordered
# print(lstTeacher[1])    # left to right indexing
# print(lstTeacher[-1])  # right to left

# # mutable
# lstTeacher.append("Nabin")
# lstTeacher.extend([1, 2])
# print(lstTeacher)
# print(lstTeacher[-1])  # right to left
# lstTeacher.remove(12)
# print(lstTeacher)
# data1 = lstTeacher.pop()
# print(lstTeacher, data1)

# # spread operator *
# l1 = [1, 3]
# l2 = [2, 4]
# l3 = l1 + l2
# l4 = [l1, l2]
# l5 = [*l1, *l2]
# print(l3, l4, l5)

# tuple: ordered but immutable
# tuple is written with () but if no () used atleast , should be used!
data1 = (1, 2, 3)
# x = list(data1)
# x.append(12)
# print(x)

# # swap two number
# (x,y) = (1,2)
# print(x, y)
# x,y = y,x
# print(x, y)

# (a, b) = (1, 2)   # multi variable assign using tuple property
# print(b*2)
# print(type(a))


# # dictionary  unordered but indexing through key and is mutable
# # dict1 = {key: value}   key: unique and immutable type  value: can be of any data type
# studentDetails = {'sam': (12, 23, 12), 'hari': (
#     32, 23, 12), 'extra': "missing"}
# print(studentDetails['hari'])  # reading the value of key
# print("The marks in Nepali is", studentDetails['hari'][2])
# # returns value of key if not found returns the default provided
# print(studentDetails.get("har", 0))
# # returns value of key if not found returns the default provided
# print(studentDetails.get("hari", 0))

# check = studentDetails.get("har", None)
# if check:
#     print("the avg marks is ", sum(check)/len(check))
# else:
#     print("No key found!")

# # If key exists when indexing the value is updated, if new key, key:value is added to dict
# studentDetails['sam'] = 12, 24, 14   # replacing with new value/ mutable
# print(studentDetails)
# studentDetails['age'] = 24           # adding new key value pair
# print(studentDetails)

# student = {
#     'name': "sandip",
#     'details': [1,2,3,5]
# }

"""
Student: Table   rows and columns
Attributes: age, phone, name are the columns
Each record/ tuple: represented by row 

1,2,3
4,2,1
5,2,1

"""
# matrix = [[1,2,3],[4,2,1],[5,2,1]]   # matrix is represented by 2D list==> list having list of rows
# print(matrix[0][2])                  # indexing first row is accessed followed by columns  list[row][column]

# Slicing similar to range syntax   list[start_index:stop_index:step]
# Start: start position and is inclusive
# Stop: exclusive ending index/position
# Step: jump value
# +ve: scanning left to right
# -ve: scanning right to left

numbers = list(range(1, 16))
print("number>>", numbers)
# enumerate(iterable, start=0)
# enumerate returns tuple from collection (index, element from collection)
numbers2 = tuple(enumerate(numbers))
# print(numbers2)
# step -ve: scan from right to left, start: -1(last) stop: 2 exclusive, upto 3
# x1 = numbers[-1:2:-2]
# print(numbers.index(4))
# print(x1)

# if start or stop value is empty, it takes min/ max  start-stop value possible // what ever
x1 = numbers[-1::-1]
x1 = numbers[:-1]
x2 = numbers[-1]
print("X1>>", x1)
print("X2>>", x2)

# # matrix is represented by 2D list==> list having list of rows
# matrix = [[1, 2, 3], [4, 2, 1], [5, 2, 1]]
# # indexing first row is accessed followed by columns  list[row][column]
# # print(matrix[0][2])
# print(matrix[:2])
# sliced = []
# for each in matrix[:2]:
#     # print(each[1:])
#     sliced.append(each[1:])
# print(sliced)

# Comprehension  List and dictionary

lst = list(range(6))
print(lst)
sqrEven = []  # what else??
for data in lst:
    if data % 2 == 0:
        sqrEven.append(data**2)
    elif data % 3 == 0:
        sqrEven.append(data*2)
    else:
        sqrEven.append(data)
print(sqrEven)

# sqrEvenC = [data**2 for data in lst if data%2 == 0]
# sqrEvenC = [data**2 if data % 2 == 0 else data for data in lst]
# sqrEvenC = [data**2 if data % 2 == 0 else data *2 if data % 3 == 0 else data for data in lst]
# print(sqrEvenC)

student = ['sandip', 'binaya', 'prajwol']
nepali = [99, 100, 90]
# dic_student = {}     # any other way??
# for each in student:
#     # updating the dict with new items from the list givem
#     dic_student[each] = len(each)
# dic_student = {var: len(var) for var in student}
# print(dic_student)

# dic_marks = {}     # any other way??
# for i in range(len(student)):
#     # updating the dict with new items from the list givem
#     dic_marks[student[i]] = nepali[i]

# dic_marks = {student[i]: nepali[i] for i in range(len(student))}

# zip(iterable1,iterable2,iterable3.....)    output: (it1.1,it2.1,it3.1), (it1.2,it2.2,it3.2)

# updated_coll = tuple(zip(student, nepali))
# print(tuple(updated_coll))
# dict_marks = {name: marks for name, marks in updated_coll}
# print(dict_marks)


# map, filter, lambda
# map/filter(fun, iterable)   map===> each element of iterable is passed to function and changes to returned value
# filter >> returns elements of iterable if function condition is fulfilled, i.e fun should return true or false

def sqr(n):
    return n**2


def add(a, b):
    return a+b


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


x1 = map(sqr, filter(is_even, lst))
print(tuple(x1))

# lambda is anonymous function

x2 = map(lambda x: x+2, lst)
print(list(x2))
x2 = map(lambda x, y: x+y, lst, lst)
print(list(x2))

x3 = map(add, lst, lst)
print(list(x3))




# file = open('./fileStatus.txt')  # relative path   os module, wd +join
# # content = file.read()
# content = file.readlines()
# file.close()

# print(content)

database101 = []
with open('./fileStatus.txt') as file:
    content = file.readlines()
    # print(content[1].strip())
    # print('test')
    for each in content:
        updated = each.strip().split('-')
        database101.append(updated)

# # print(database101)
# # print(database101[1][2])
# print(database101[1:])
# sum_ = 0
# for each in database101[1:]:
#     sum_ += int(each[1])
# avg = sum_//len(database101[1:])
# print(avg)

with open('sample.txt', 'w') as file:
    file.write('sandip\n')
    file.write(str(101))