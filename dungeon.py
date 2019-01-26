import random
import math


class Room:
    room_count = 0

    def __init__(self):
        self.index = Room.room_count+1
        self.left = None
        self.right = None
        self.front = None
        self.back = None
        Room.room_count += 1


class Dungeon:
    """Contains rooms for game stages."""
    current_room = None
    first_room = None

    def __init__(self, room_lim=10):
        self.first_room = Room()
        self.room_limit = room_lim
        self.current_room = self.first_room

    def generate_map(self):
        """Generates random dungeon maps."""
        while (Room.room_count <= self.room_limit):
            self.random_integer = random.randint(1, 10)
            if(self.random_integer < 6):
                self.current_room.front = Room()
                self.current_room.front.back = self.current_room
                self.current_room = self.current_room.front
            elif(self.random_integer == 7 or self.random_integer == 8):
                self.current_room.left = Room()
                self.current_room.left.back = self.current_room
                self.current_room = self.current_room.left
            elif(self.random_integer == 9 or self.random_integer == 10):
                self.current_room.right = Room()
                self.current_room.right.back = self.current_room
                self.current_room = self.current_room.right
        self.current_room = self.first_room

    def next_room(self, direction):
        if(direction == 1 and self.current_room.front != None):
            self.current_room = self.current_room.front
        elif(direction == 2 and self.current_room.left != None):
            self.current_room = self.current_room.left
        elif(direction == 3 and self.current_room.right != None):
            self.current_room = self.current_room.right
        elif(direction == 4 and self.current_room.back != None):
            self.current_room = self.current_room.back
        else:
            self.current_room = self.current_room


def main():
    d = Dungeon()
    d.generate_map()
    inp = None
    while(inp != 0):
        print("Current Room: " + str(d.current_room.index))
        inp = int(input())
        d.next_room(inp)


if __name__ == "__main__":
    main()
