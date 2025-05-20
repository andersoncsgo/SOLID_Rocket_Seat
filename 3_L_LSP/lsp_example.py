class Animal:
    def comer(self):
        print("O animal esta comendo")

    def andar(self):
        print("O animal esta andando na jaula")
    
class Felino(Animal):
    def lamber(self):
        print("O felino esta lambendo o seu pelo")

class Leao(Felino):
    def rugir(self):
        print("o leao esta rugindo alto !!!")

class Pessoa:
    def observa(self, animal: Animal):
        animal.comer()

renatinho = Pessoa()
leao = Leao()
animal = Animal()
felino = Felino()


renatinho.observa(leao)