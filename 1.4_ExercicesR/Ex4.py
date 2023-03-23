def sum_numbers(liste):
    list2 = []
    ind = 0
    for i in liste :
        if i == "Green" or i == "White" or i == "Black":
            list2.append(i)
            ind+=1
    return list2

print(sum_numbers(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']))