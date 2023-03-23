sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
print("Original list ", sample_list)

count = dict()

for item in sample_list:
    if item in count:
        count[item] += 1
    else :
        count[item] = 1


print("Printing count of each item ", count)