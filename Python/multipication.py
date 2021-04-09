# list1 = [2, 4, 5]
# list2 = [2, 3, 6]
# mult_list = []

# for i in range(0,len(list1)):
#     mult_list.append(list1[i]*list2[i])

# print(list1, "X", list2, "=", mult_list)

matrixOne = [[1, 3], [2, 4]] 
matrixTwo = [[5, 2], [1, 0]]
matrixSum = []
# matrixOne[0][0] + matrixTwo[0][0]
# [0][0] + [0][0] = 1 + 5 = 6
# [0][1] + [0][1] = 3 + 2 = 5
# [1][0] + [1][0] = 2 + 1 = 3
# [1][1] + [1][1] = 4 + 0 = 4
for indexOne in range(2): 
    matrixThree = []
    for indexTwo in range(2): 
        matrixThree.append(matrixOne[indexOne][indexTwo] + matrixTwo[indexOne][indexTwo])
        # matrixThree = [3, 4]
    matrixSum.append(matrixThree)
    # matrixSum = [[6, 5], [3, 4]]
print(matrixSum)
