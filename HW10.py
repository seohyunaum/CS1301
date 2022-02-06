"""
Georgia Institute of Technology - CS1301
Homework 10 - Object Oriented Programming
"""

class Pokemon:
    def __init__(self, name, level, atype, bag, health = 50.0, isAlive = True):
        self.name = name
        self.level = level
        self.type = atype
        self.bag = bag
        self.health = health
        self.isAlive = isAlive
    
    def loseHealth(self, num):
        if self.isAlive:
            self.health -= 5*num
        if self.health <= 0:
            self.isAlive = False
    
    def gainHealth(self):
        if self.isAlive == False:
            print("{} has fainted! Cannot gain health!".format(self.name))
        elif self.bag.healthPotion == 0:
            print("Sorry, {} has no health potions!".format(self.name))
        elif self.health <= 30.0:
            self.health += 20.0
            self.bag.healthPotion -= 1
        else:
            self.health = 50.0
            self.bag.healthPotion -= 1

    def surrender(self):
        self.bag.whiteFlag = True

    def __eq__(self, other):
        return self.type == other.type and self.name == other.name

    def __str__(self):
        return "This is {} type Pokemon {} with level {}, current health is {}.".format(self.type, self.name, str(self.level),  str(self.health))
        
#########################################################


class Bag:
    def __init__(self, healthPotion, whiteFlag):
        self.healthPotion = healthPotion
        self.whiteFlag = whiteFlag
        
    
    #provided
    def __eq__(self, other):
        return self.healthPotion == other.healthPotion and self.whiteFlag == other.whiteFlag


#########################################################


class Lobby:
    def __init__(self, roomName, pokeA, pokeB):
        self.roomName = roomName
        self.pokeA = pokeA
        self.pokeB = pokeB
    
    def gameOver(self):
        if (self.pokeA.isAlive == False and self.pokeB.isAlive == False) or (self.pokeA.bag.whiteFlag == True and self.pokeB.bag.whiteFlag == True):
            print("It's a tie!")
        elif (self.pokeA.isAlive == False or self.pokeA.bag.whiteFlag == True) and self.pokeB.isAlive:
            print("{} won the battle".format(self.pokeB.name))
            self.pokeB.level += 1
        elif (self.pokeB.isAlive == False or self.pokeB.bag.whiteFlag == True) and self.pokeA.isAlive:
            print("{} won the battle".format(self.pokeA.name))
            self.pokeA.level += 1

    def battle(self):
        one = self.pokeA.type
        two = self.pokeB.type
        self.pokeA.bag.whiteFlag == False
        self.pokeB.bag.whiteFlag == False
        if (one == "Fire" and two == "Water") or (one == "Water" and two == "Grass") or (one == "Grass" and two == "Fire"):
            self.pokeA.loseHealth(2)
            self.pokeB.loseHealth(0.5)
        elif (one == "Grass" and two == "Water") or (one == "Fire" and two == "Grass") or (one == "Water" and two == "Fire"):
            self.pokeA.loseHealth(0.5)
            self.pokeB.loseHealth(2)
        elif one == two:
            self.pokeA.loseHealth(1)
            self.pokeB.loseHealth(1)
        self.gameOver()


    def __eq__(self, other):
        return self.roomName == other.roomName
            




















        
