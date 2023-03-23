liste  = [17,38,10,25,72]

#sort numbers
print(sorted(liste))

#add 12
liste.append(12)
print(liste)

#Reverse list

liste.reverse()
print(liste)

# afficher l'indice de l'element 17

indice = liste.index(17)
print("index of 17 is ", indice)

# enlever l'element 38

liste.remove(38)
print(liste)

#sous liste from 2 to 3
print(liste[2:3])

#dubut to 2eme element
print(liste[:3])

#from 3 element to the end
print(liste[3::])

#sous liste kamla
print(liste[:])

#last element using indexage negatif
print(liste[-1])