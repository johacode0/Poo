class EtreVivant:
    ESPACE_ETREVIVANT = "etrevivant no identifié "

    def affecheretrevivant(self):
        print("etrevivant: ", self.ESPACE_ETREVIVANT)


class chat(EtreVivant):
    ESPACE_ETREVIVANT = "etrevivant chat "


class personne(EtreVivant):
    ESPACE_ETREVIVANT = "etrevivant humain "

    def __init__(self, nom: str = "", age: int = 0, genre: bool = True):
        self.nom = nom
        self.age = age
        self.genre = genre
        if nom == "":
            self.demanerNom()
        print("constructeur ", self.nom)

    def Sepresenter(self):
        print("je suis ", self.nom, "j'ai", self.age, "ans")
        genre = "masculin" if self.genre else "feminin"
        print("genre:", genre)
        e = "" if self.genre else "e"
        if self.age != 0:
            if self.majeur():
                print("je suis majeur" + e)
            else:
                print("je suis mineur" + e)

    def demanerNom(self):
        self.nom = input("donner vtre nom : ")

    def majeur(self):
        return self.age >= 18


class etudiant(personne):
    def __init__(
        self,
        nom: str = "",
        age: int = 0,
        genre: bool = True,
        etude: str = "",
    ):
        self.nom = nom
        self.age = age
        self.genre = genre
        self.etude = etude
        if nom == "":
            self.demanerNom()
        print("constructeur ", self.nom)

    def Sepresenter(self):
        super().Sepresenter()
        print("je suis etudiant en ", self.etude)


p = etudiant("al", 22, False, "erer")
p.Sepresenter()
# l_p = [personne("ali", 30, True), personne("ahmed", 10, False), personne()]
# p1 = personne("ali", 30, True)
# p2 = personne("ahmed", 10, False)
# l_p.append(personne(age=14))
# for p in l_p:
#     p.Sepresenter()
