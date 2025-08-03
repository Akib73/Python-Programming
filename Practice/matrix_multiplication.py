matrix_1x3 = [[1, 2, 3]]  # 1 row, 3 columns
matrix_3x3 = [[4, 5, 6],
              [7, 8, 9],
              [10, 11, 12]]

# Perform matrix multiplication
result = [[0 for _ in range(len(matrix_3x3[0]))] for _ in range(len(matrix_1x3))]

for i in range(len(matrix_1x3)):
    for j in range(len(matrix_3x3[0])):
        for k in range(len(matrix_3x3)):
            result[i][j] += matrix_1x3[i][k] * matrix_3x3[k][j]

print("Result of 1x3 * 3x3 multiplication:")
for row in result:
    print(row)