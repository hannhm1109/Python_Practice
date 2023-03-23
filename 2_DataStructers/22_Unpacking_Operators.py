values = list(range(5))
values = [*range(5), *"Hello"]
print(values)

first = [1,2]
second = [3]
value = [*first , "a" , *second, *"Hello"]
print(value)

lwl = {"x" : 1}
tani = {"x" : 10 , "y" : 2}
combined = {**lwl, **tani,"z" : 1}
print(combined)