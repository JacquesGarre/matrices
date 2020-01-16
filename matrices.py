import numpy as np 
from random import randint


class Matrice(object):

    def __init__(self):
        self.x = self.getIntFromUser("x")
        self.y = self.getIntFromUser("y")
        self.value = self.buildRandomMatrice()

    # Asks a user to input an int
    def getIntFromUser(self, name):
        print("Veuillez entrer un nombre entier correspondant à l'axe {} de la matrice :".format(name))
        while True:
            try:
                i = int(input())
                if i <= 0:
                    print("{} doit être supérieur à 0, veuillez recommencer votre saisie".format(i))
                break
            except:
                print("{} n'est pas un entier, veuillez recommencer votre saisie".format(i))
        return i

    # Builds the matrice from user input
    def buildMatrice(self):
        print("Veuillez entrer les {} valeurs de la matrice:".format(self.x * self.y))
        matrice = []
        for i in range(1, self.x + 1):
            line = []
            for j in range(1, self.y + 1):
                line.append(input("Valeur de a{}{}:".format(i, j)))
            matrice.append(line)
        return np.array(matrice)
    
     # Builds the matrice from random values
    def buildRandomMatrice(self):
        matrice = []
        for i in range(1, self.x + 1):
            line = []
            for j in range(1, self.y + 1):
                value = randint(0, 10)
                line.append(value)
            matrice.append(line)
        return np.array(matrice)

    # Returns the value at x,y coordinates in the matrice
    def getValue(self, xAsked, yAsked):
        return self.value[xAsked-1][yAsked-1]

    # A column matrice is a matrice that has a unique column
    @property
    def isColumnMatrice(self):
        return True if self.y == 1 else False
    
    # A line matrice is a matrice that has a unique line
    @property
    def isLineMatrice(self):
        return True if self.x == 1 else False

    # A squared matrice is a matrice that has same amount of lines and columns
    @property
    def isSquaredMatrice(self):
        return True if self.y == self.x else False

    # returns Diagonale
    @property
    def diagonale(self):
        if self.isSquaredMatrice:
            #11, 22, 33, 44, 55
            for i, j in range(1, self.x + 1):
                print(i, j)
        else:
            return None


matrice = Matrice()
print(matrice.value)
matrice.diagonale(self)
