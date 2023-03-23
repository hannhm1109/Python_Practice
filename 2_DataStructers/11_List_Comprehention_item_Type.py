items = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 12),
]

#filtered = list(filter(lambda item: item[1] >= 10,items))

#List comprehentions are more functional and Readable

filtered = [item for item in items if item[1] >= 10]

print(filtered)