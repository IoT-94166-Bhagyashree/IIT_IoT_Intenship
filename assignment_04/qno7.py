matrix1 = [
    [10, 9, 8, 4],
    [4, 6, 17, 5],
    [5, 4, 6, 12]
]

matrix2 = (
    (12, 11, 10, 9),
    (8, 7, 6, 5),
    (4, 3, 2, 1)
)

def matrix_operations(m1, m2):
    add_result = []
    sub_result = []

    for i in range(len(m1)):
        add_row = []
        sub_row = []
        for j in range(len(m1[0])):
            add_row.append(m1[i][j] + m2[i][j])
            sub_row.append(m1[i][j] - m2[i][j])
        add_result.append(add_row)
        sub_result.append(sub_row)

    return add_result, sub_result

addition, subtraction = matrix_operations(matrix1, matrix2)

print("Addition Result:")
for row in addition:
    print(row)

print("\nSubtraction Result:")
for row in subtraction:
    print(row)
