#!/data/data/com.termux/files/usr/bin/python
import os
import time
import random
import math


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


class Screen:
    playername = None
    enemyname = None
    content = "Test Text"
    def draw(self,playerobject,enemyobject):
        self.playername = playerobject.getname()
        self.playerhp = playerobject.gethealth()
        self.playermp = playerobject.getmagic()
        self.enemyname = enemyobject.getname()
        self.enemyhp = enemyobject.gethealth()
        self.enemymp = enemyobject.gethealth()
        if os.name == 'nt':
            os.system("""cls""")
        else:
            os.system("""clear""")
        for i in range(50):
            print("-", end="")
        if self.playername != None:
            print("")
            print(self.playername)
            print("\tHP: ", end="")
            for i in range(math.floor(self.playerhp/10)):
                print("#", end="")
            print("\t\tMP: ", end="")
            for i in range(math.floor(self.playermp/10)):
                print("#", end="")
            print("")
            for i in range(50):
                print("-", end="")
        for i in range(20):
            print("")
        if self.enemyname != None:
            for i in range(50):
                print("-", end="")
            print("")
            print(self.enemyname)
            print("\tHP: ", end="")
            for i in range(math.floor(self.enemyhp/10)):
                print("#", end="")
            print("\t\tMP: ", end="")
            for i in range(math.floor(self.enemymp/10)):
                print("#", end="")
            print("")
        for i in range(50):
            print("-", end="")
        print("\033[5;1H")
        for i in list(self.content):
            time.sleep(0.063)
            print(i, end="", flush=True)
        print("")

    def resetcontent(self, texty):
        self.content = texty

    def appendline(self, texty):
        self.content = self.content + "\n" + texty

    def append(self, texty):
        self.content = self.content + texty


def main():
    a = Character("Lupin III", 100, 100, 10)
    b = Character("Police", 50, 50, 5)
    sc = Screen()
    sc.resetcontent("Welcome to Text RPG!!")
    sc.draw(a,b)
    input()
    sc.resetcontent("Press any key to start game.")
    sc.draw(a,b)
    input()
    event = a.attack(b)
    sc.resetcontent("a used ATTACK on b!!")
    if event == 1:
        sc.appendline("Super Effective!!")
    elif event == 2:
        sc.appendline("Partially Blocked!!")
    else:
        sc.appendline("Fully Blocked!!")
    sc.draw(a,b)
    input()
    if os.name == 'nt':
        os.system("""cls""")
    else:
        os.system("""clear""")


if __name__ == "__main__":
    main()
