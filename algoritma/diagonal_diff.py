from typing import List


def diagonal_diff(matrix: List):
    d1 = 0
    d2 = 0
    l = len(matrix)
    for i in range(l):
        d1 += matrix[i][i]
        d2 += matrix[i][l - i - 1]

    return d1-d2


if __name__ == "__main__":
    matrix = [[1, 2, 0], [4, 5, 6], [7, 8, 9]]
    print(diagonal_diff(matrix))
