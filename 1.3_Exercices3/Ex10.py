a = int(input("enter number :"))
b = int(input("enter number :"))

#for i in range(1,a):
#   if a % i == 0 and b % i == 0:
#       print(i)

newlist = []
for i in range(1, a):
    if a % i == 0 and b % i == 0:
        newlist.append(i)
print(newlist[len(newlist)-1])