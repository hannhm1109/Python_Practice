first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

Intersection = first_set.intersection(second_set)

print("Intersection is :", Intersection)

for item in Intersection :
    first_set.remove(item)

print("First Set after removing common element : ",first_set)