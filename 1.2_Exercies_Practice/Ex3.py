def multListe(L):

    new_list = L[:]

    for i in range(len(new_list)):
        if i % 2 == 0:
            new_list[i] = new_list[i] * 2
        else :
            new_list[i] = new_list[i] * 3
    return new_list


L = [3, 2, 7, 11, 5, 3]
print(multListe(L))