def puissance(a, b):
    result = 1
    for i in range(b):
        result = result * a
    return result

a = int(input("enter number 1:"))
b = int(input("enter number 2:"))

print(puissance(a,b))