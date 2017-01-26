# Matrix Representation Example
matrix_a = [[3, 6], [4, 5]] # List로 표현했을 경우
matrix_b = [(3, 6), (4, 5)] # Tuple로 표현했을 경우
matrix_c = {(0 ,0): 3, (0 ,1): 6, (1 ,0): 4, (1 ,1): 5} # dict 표현했을 경우


# Matrix Addition
matrix_a = [[3, 6], [4, 5]]
matrix_b = [[5, 8], [6, 7]]
result = [[sum(row) for row in zip(*t)] for t in zip(matrix_a, matrix_b)]

print(result)

# Scalar-Matrix Product
matrix_a = [[3, 6], [4, 5]]
alpha = 4
result = [[alpha * element for element in t] for t in matrix_a]

print(result)

# Matrix Transpose
matrix_a = [[1, 2, 3], [4, 5, 6]]
result = [ [element for element in t] for t in zip(*matrix_a) ]
print (result)

# Matrix Product
matrix_a = [[1, 1, 2], [2, 1, 1]]
matrix_b = [[1, 1], [2, 1], [1, 3]]
result = [[sum(a * b for a, b in zip(row_a, column_b)) for column_b in zip(*matrix_b)] for row_a in matrix_a]

print(result)
