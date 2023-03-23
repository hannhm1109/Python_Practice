d = ["Lundi","Mardi","Mercredi","Jeudi","Vendredi","Samedi","Dimanche"]
print(d)

print(d[4])

temp= d[0]
d[0] =  d[len(d)-1]
d[len(d)-1] = temp

print(d)

for i in range(12):
    print(d[len(d)-1])