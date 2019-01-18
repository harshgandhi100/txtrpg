import random
from math import ceil


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


class BaseCharacter:

    def __init__(self, name, hp, mp, p_attack, p_defence, m_attack, m_defence):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.p_attack = p_attack
        self.p_defence = p_defence
        self.m_attack = m_attack
        self.m_defence = m_defence

    def light_attack(self, target):
        fail_chance = random.random()
        damage = 0
        if(fail_chance>=0.2):
            percent_damage = random.uniform(0.5, 1.0)
            # print(percent_damage)
            damage = ceil((self.p_attack - target.p_defence) * percent_damage)
            # print('damage:' + str(damage))
        target.hp = target.hp - damage

    def heavy_attack(self, target):
        print("heavy attack")


class Warrior(BaseCharacter):
    def __init__(self, name):
        super(Warrior, self).__init__(name, 1000, 1000, 100, 100, 100, 100)


class Mage(BaseCharacter):
    def __init__(self, name):
        super(Mage, self).__init__(name, 800, 1200, 50, 50, 200, 200)


class Goblin(BaseCharacter):
    def __init__(self, name):
        super(Goblin, self).__init__(name, 500, 500, 50, 50, 50, 50)

# def main():
#     warrior1 = Warrior('Warrior')
#     warrior2 = Goblin('Goblin')
#     for i in range(5):
#         warrior1.light_attack(warrior2)
#         print(warrior2.name)
#         print(warrior2.hp)


# if __name__ == "__main__":
#     main()
