matrix = [[1,2,3],[3,7,8]]

empty = []
for i in range(len(matrix[0])):
    t_matrix = []
    for x in matrix:
        element = x[i]
        t_matrix.append(element)
    
    empty.append(t_matrix)

print(empty)