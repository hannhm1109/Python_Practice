sample_list = [87, 52, 44, 53, 54, 87, 52, 53]

print("Original list", sample_list)

unique_items = list()

for item in sample_list:
    if item not in unique_items:
        unique_items.append(item)

print("Unique items : ", unique_items)

#sample_list = list(set(sample_list))
#print("unique list", sample_list)


tuple_list = tuple(unique_items)
print("tuple ", tuple_list)

print("min :", min(tuple_list))
print("max :", max(tuple_list))

