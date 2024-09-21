class Animal:
    def __init__(self, nome):
        self.nome = nome
    
    def som(self):
        print("Som genérico")

class cachorro(Animal):
    def som(self):
        print("Au Au")

class gato(Animal):
    def som(self):
        print("Miau")

cachorro = cachorro("Juninho Golado")
gato = gato("Jurema")
cachorro.som()  
gato.som()  
