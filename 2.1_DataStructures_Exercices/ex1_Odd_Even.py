l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

final_list = list()

print("Element at odd-index positions from list one :")
odd = l1[1::2]
print(odd)
print("Element at even-index positions from list two :")
even = l2[0::2]
print(even)

print("Printing Final third list")
final_list.extend(odd)
final_list.extend(even)

print(final_list)
