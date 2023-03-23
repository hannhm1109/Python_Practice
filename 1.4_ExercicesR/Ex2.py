def max_liste(liste):
    maximum = liste[0]
    for i in liste :
        if i > maximum :
            maximum = i
    return maximum 

print(max_liste([1,5,6,7,8]))