def printZeroPositions(matrix):
    n = len(matrix)
    m = len(matrix[0])

    for i in range(n):
        for j in range(m):
            print(matrix[i][j], end=" ")
           
        print()  

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                print(f'Position ({i}, {j}) has a zero')

matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
printZeroPositions(matrix)
