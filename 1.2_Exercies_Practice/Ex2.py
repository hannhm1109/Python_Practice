def depZero(L):
    
    zero = []
    new_list = []

    for num in L:
        if num == 0:
            zero.append(num)
        else :
            new_list.append(num)
    zero += new_list
    return zero

L = [7, 0, 11, 0, 25, 16, 0, 14]
print(depZero(L))
