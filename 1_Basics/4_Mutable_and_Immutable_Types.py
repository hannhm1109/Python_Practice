#variables are immutable if we change the variable a new memory location will be set
#list are mutable  u can change them in the same memory location x address

x = 1
print(id(x))
x = x + 1
print(id(x))


y = [1,2,3]
print(id(y))
y.append(4)
print(id(y))