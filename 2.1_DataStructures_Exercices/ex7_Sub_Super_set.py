first_set = {57, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

print("First Set ", first_set)
print("Second Set ", second_set)

subset = first_set.issubset(second_set)
subset2 = second_set.issubset(first_set)

print("First set is subset of second set :",subset)
print("Second set is subset of First set :",subset2)


superset = first_set.issuperset(second_set)
superset2 = second_set.issuperset(first_set)

print("First set is superset of second set :",superset)
print("Second set is superset of First set :",superset2)

if first_set.issubset(second_set):
    first_set.clear()

if second_set.issubset(first_set):
    second_set.clear()


print("First Set ", first_set)
print("Second Set ", second_set)