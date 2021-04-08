matrixone = [[1, 3], [2, 4]]
matrixtwo = [[5, 2],[1, 0]]
matrixsum = []

matrixsum = [[]], [[]]

# [0][0] + [0][0]
# [0][1] + [0][1]
# [1][0] + [1][0]
# [1][1] + [1][1]

for indexone in range(2):
    matrixthree = []
    for indextwo in range(0, 2, 1):
        matrixthree.append(matrixone[indexone][indextwo]) + matrixtwo[indexone][indextwo]) 

        matrixsum.append(matrixthree)


        print(matrixsum)

