test_list1 = [2, 4, 5] 
test_list2 = [2, 3, 6]

print ('original list 1 :' + str (test_list1))  
print ('original list 1 :' + str (test_list2))

res_list = []
for i in range (0, len(test_list1)) :
    res_list.append(test_list1 [i] * test_list2 [i])

print ('sort :' + str (res_list))






