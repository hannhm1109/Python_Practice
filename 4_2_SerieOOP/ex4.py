class CompteBancaire:
    def __init__(self, numeroCompte, nom, solde):
        self.numeroCompte = numeroCompte
        self.nom = nom
        self.solde = solde
    
    def versement(self , montant):
        self.solde += montant
        print("versement de {} effectuee sur le compte {} de {}".format(self.solde, self.numeroCompte, self.nom))

    def retrait(self, montant):
        if self.solde >= montant:
            self.solde -= montant
            print("Retrait de {} euros effectué sur le compte {} de {}".format(montant, self.numeroCompte, self.nom))
        else:
            print("Retrait impossible : solde insuffisant sur le compte {} de {}".format(self.numeroCompte, self.nom))
    
    def afficher(self):
        print("Détails du compte bancaire :")
        print("Numéro de compte : {}".format(self.numeroCompte))
        print("Nom du propriétaire : {}".format(self.nom))
        print("Solde : {} euros".format(self.solde))


# création d'un compte bancaire et affichage de ses informations
compte1 = CompteBancaire(123456, "Alice", 1000)
compte1.afficher()

# opérations sur le compte bancaire
compte1.versement(500)
compte1.retrait(2000)
compte1.retrait(700)

# affichage des informations mises à jour du compte bancaire
compte1.afficher()

