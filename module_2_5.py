def get_matrix(n, m, value): # n = строки, m = столбцы, value = значения
    matrix = []
    for a in range(n):
        matrix.append([])
        for b in range(m):
            matrix[a].append(value)
    return matrix
result = get_matrix(5, 3, 10)
print(result)
result_2 = get_matrix(6, 5, 15)
print(result_2)
resilt_3 = get_matrix(2, 2, 25)
print(resilt_3)

