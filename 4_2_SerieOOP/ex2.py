class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def perimetre(self):
        return 2 * (self.longueur + self.largeur)
    
    def surface(self):
        return self.longueur * self.largeur
    
    def affichage(self):
        print("rectangle de longueur {} et largeur {}".format(self.longueur, self.largeur))
        print("Perimetre {}".format(self.perimetre))
        print("Surface {}".format(self.surface))

    def get_longueur(self):
        return self.__longueur
    
    def set_longueur(self, longueur):
        self.__longueur = longueur

    def get_largeur(self):
        return self.__largeur
    
    def set_largeur(self, largeur):
        self.__largeur = largeur


rect = Rectangle(5, 3)
# rect.affichage()

# p = rect.perimetre()
# s = rect.surface()

# print("perimetre {} surface {}".format(p,s))


rect.set_longueur(6)
rect.set_largeur(4)

print("L :", rect.get_longueur)
print("l :", rect.get_largeur)


p = rect.perimetre()
s = rect.surface()

print("Le perimeter {} surface est {}".format(p, s))
