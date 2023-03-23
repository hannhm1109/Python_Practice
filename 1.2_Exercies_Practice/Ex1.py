def SuppNegatif(L):
    new_list = L[:]
    for num in L:
        if num < 0:
            new_list.remove(num)
    return new_list


    
L = [1,2,-9,-6,-5,8,4]
print(SuppNegatif(L))


