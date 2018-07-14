#!/data/data/com.termux/files/usr/bin/python
import os
import time
import random
from screen import Screen
from character import Character

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
    while a.gethealth() > 0 and b.gethealth() > 0:
        event = a.attack(b)
        sc.resetcontent("a used ATTACK on b!!")
        if event == 1:
            sc.appendline("Super Effective!!")
        elif event == 2:
            sc.appendline("Partially Blocked!!")
        else:
            sc.appendline("Fully Blocked!!")
        sc.draw(a,b)
        time.sleep(1)
        event = b.attack(a)
        sc.resetcontent("b used ATTACK on a!!")
        if event == 1:
            sc.appendline("Super Effective!!")
        elif event == 2:
            sc.appendline("Partially Blocked!!")
        else:
            sc.appendline("Fully Blocked!!")
        sc.draw(a,b)
        time.sleep(1)

    if a.gethealth() > 0:
        sc.resetcontent(a.getname()+" Won!!!")
    else:
        sc.resetcontent(b.getname()+" Won!!!")
    sc.draw(a,b)
    input()

    if os.name == 'nt':
        os.system("""cls""")
    else:
        os.system("""clear""")


if __name__ == "__main__":
    main()
