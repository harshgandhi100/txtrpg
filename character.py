import random

class Character:
    health = 100
    magic = 100
    power = 10
    name = "Player 1"

    def __init__(self, name, hp, mp, pp):
        self.health = hp
        self.magic = mp
        self.power = pp
        self.name = name

    def attack(self, target):
        feedback = target._damage(self.power)
        return feedback

    def gethealth(self):
        return (self.health)

    def getmagic(self):
        return (self.magic)

    def getname(self):
        return (self.name)

    def _damage(self, damagepoints):
        fate = random.choice([1, 2, 3])
        if fate == 1:
            self.health = self.health - damagepoints
        elif fate == 2:
            self.health = self.health - (damagepoints/2)
        return fate