size = int(input("Введите размерность квадратной матрицы: "))

matrix = []
for i in range(size):
    row = [j + 1 for j in range(size)]
    matrix.append(row)

print("Исходная матрица:")
for row in matrix:
    print(row)

for i in range(size):
    for j in range(i + 1, size):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

print("Транспонированная матрица:")
for row in matrix:
    print(row)