numbers = [3,51,2,8,6]
print(sorted(numbers, reverse=True))
print(numbers)

items = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 12),
]

def sort_item(item):
    return item[1]

items.sort(key=sort_item)
print(items)