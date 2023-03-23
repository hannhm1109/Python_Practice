values = {}
for x in range(5):
    values[x] = x * 2

# same as above but more efficient
# if u run this code u will get an error bcz of the first 2 lines delete them then run it !
values = {x: x * 2 for x in range(5)}
print(values)