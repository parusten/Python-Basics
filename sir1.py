# # matrix is represented by 2D list==> list having list of rows
matrix = [[1, 2, 3], [4, 2, 1], [5, 2, 1]]
# indexing first row is accessed followed by columns  list[row][column]
print(matrix[0][2])
print(matrix[:2])
sliced = []
for each in matrix[:2]:
    print(each[1:])
#     sliced.append(each[1:])
# print(sliced)