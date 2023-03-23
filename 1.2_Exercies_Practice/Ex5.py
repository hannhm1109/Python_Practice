def supprimeDoublon(L):
    new_list = []
    for num in L:
        if num not in new_list:
            new_list.append(num)
    return new_list

L = [3,4,5,3,4,5,1]
print(supprimeDoublon(L))