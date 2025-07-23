import random as rnd

class user:
    def __init__(self, name = "unknown"):
        self.name = name
        self.chance = 1
        self.skill = rnd.randint(1, 10)

        self.isMurderer = False
        self.isSheriff = False
        self.isAlive = True