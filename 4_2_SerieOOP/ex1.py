import math

class Point:
    def __init__(self,x=0.0,y=0.0):
        self.__x = x
        self.__y = y
    
    def deplace(self, dx, dy):
        self.__x += dx
        self.__y += dy
    
    def affiche(self):
        print("coordonne cartisienne : ({}, {})".format(self.__x, self.__y))

    def saisir(self):
        self.__x = float(input("entrer la coordonne x :"))
        self.__y = float(input("entrer la coordonne y :"))

    def distance(self, autre_point):
        dx = self.__x - autre_point.__x
        dy = self.__y - autre_point.__y
        return math.sqrt(dx ** 2 + dy **2)
    
    def milieu(self, autre_point):
        x_milieu = (self.__x + autre_point.__x) / 2.0
        y_milieu = (self.__y + autre_point.__y) / 2.0
        return Point(x_milieu, y_milieu)
    
# création de deux points et affichage de leurs coordonnées
p1 = Point(1.0, 2.0)
p2 = Point()
p1.affiche()
p2.affiche()

# déplacement de p1 et affichage de ses nouvelles coordonnées
p1.deplace(3.0, -1.5)
p1.affiche()

# saisie des coordonnées de p2 et affichage de ses coordonnées
p2.saisir()
p2.affiche()

# calcul de la distance entre les deux points et affichage du résultat
dist = p1.distance(p2)
print("Distance entre les deux points : {}".format(dist))

# calcul du milieu entre les deux points et affichage des coordonnées du milieu
milieu = p1.milieu(p2)
milieu.affiche()
