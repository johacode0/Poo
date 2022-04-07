class Product:
    def __init__(self, name: str = "", price: float = 0, quantity: int = 0, solder: float = 0,):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.solder = solder

    def prix(self):
        prix = self.price - (self.price*self.solder)/100
        return prix*self.quantity


class Client:
    def __init__(self, name: str = "", gender: bool = False):
        self.name = name
        self.gender = gender

    def person(self):
        genre = "Mr" if self.gender else "Mme"
        print(genre, self.name)


class AchatClient:
    def __init__(self, person: Client, list: Product = []):
        self.person = person
        self.list = list

    def facture(self):
        s = 0
        for p in self.list:
            print("le prix de", p.name, ":", p.prix())
            s += p.prix()
        self.person.person()
        print("la somme total", s)


c = Client("Ahmed", True)
l = [Product("chambo", 10, 10, 10), Product(
    "bimo", 10, 2, 0), Product("fruit", 20, 1, 0)]
a = AchatClient(c, l)
a.facture()
