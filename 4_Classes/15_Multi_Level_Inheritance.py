class Animal:
    def eat(self):
        print("eat")

class Bird(Animal):
    def fly(self):
        print("fly")

#chicken is a bird but can't fly this made inheritance complicated 
#that's why we shouldn't use it a lot
class Chicken(Bird):
    pass 