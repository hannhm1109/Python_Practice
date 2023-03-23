def remove_element(liste):
      
    list_final = []
    liste2 = [0, 4, 5]
    for i in liste:
        if liste.index(i) not in liste2 :
            list_final.append(i)
    return list_final


liste =  ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print(remove_element(liste))