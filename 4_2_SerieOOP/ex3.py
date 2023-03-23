class Livre:
    def __init__(self, titre, auteur, prix):
        self.titre = titre
        self.auteur = auteur
        self.prix = prix

    def affiche(self):
        print("titre : {}".format(self.titre))
        print("auteur : {}".format(self.auteur))
        print("prix : {}".format(self.prix))


li = Livre("Hamilton","han",3400)

li.affiche()