numbers = list(range(1, 16))
print("number>>", numbers)
# enumerate(iterable, start=0)
# enumerate returns tuple from collection (index, element from collection)
# numbers2 = tuple(enumerate(numbers))
# print(numbers2)
# # # step -ve: scan from right to left, start: -1(last) stop: 2 exclusive, upto 3
# x1 = numbers[-1:2:-2]
# print(numbers.index(4))
# print(x1)


x1 = numbers[-1::-1]
# x1 = numbers[:-1]

