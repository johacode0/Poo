# création de la class eleve
class eleve:
    def __init__(self, nom:str="", age: int=0, genre: bool=True):
        self.nom = nom
        self.age = age
        self.genre = genre
    def sepresenter(self):
        g='Mr' if self.genre else 'Mme'
        print('bienvenu', g,":" ,self.nom, 'votre age: ', self.age)
# fin création de la class eleve
class matiere:
    def __init__(self, nom:str="", note:float=0, c:int=0):
        self.nom = nom
        self.note = note
        self.c = c
class resultat:
    def __init__(self,e:eleve, lm:matiere=[]):
        self.e = e
        self.lm = lm
    def resultat(self):
        s=0
        d=0
        r=0
        for v in self.lm:
            s+=v.note*v.c
            d+=v.c
            r=s/d
        print("le résultat final: ", r)
e=eleve("hasna", 17, False)
o=eleve("hasan", 22, True)
l=[matiere("math", 17, 5),
matiere("arabe", 18, 2),
matiere("fr", 14, 3)]
u=[matiere("math", 6, 5),
matiere("arabe", 10, 2),
matiere("fr", 2, 3)]
r1=resultat(e,l)
r2=resultat(o,u)
r1.resultat()
r2.resultat()