for x in range(5):
    values[x] = x * 2

# same as above but more efficient

values = {x: x * 2 for x in range(5)}
print(values)