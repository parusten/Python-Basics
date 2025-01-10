# Comprehension  List and dictionary

lst = list(range(6))
print(lst)
sqrEven = []  # what else??
# for data in lst:
#     if data % 2 == 0:
#         sqrEven.append(data**2)
#     elif data % 3 == 0:
#         sqrEven.append(data*2)
#     else:
#         sqrEven.append(data)
# print(sqrEven)

sqrEvenC = [data**2 for data in lst if data%2 == 0]
sqrEvenC = [data**2 if data % 2 == 0 else data for data in lst]
sqrEvenC = [data**2 if data % 2 == 0 else data *2 if data % 3 == 0 else data for data in lst]
print(sqrEvenC)