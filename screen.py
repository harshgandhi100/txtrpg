import math
import os
import time

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
        self.enemymp = enemyobject.getmagic()
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
            time.sleep(0.030)
            print(i, end="", flush=True)
        print("")

    def resetcontent(self, texty):
        self.content = texty

    def appendline(self, texty):
        self.content = self.content + "\n" + texty

    def append(self, texty):
        self.content = self.content + texty