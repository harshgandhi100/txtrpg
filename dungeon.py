import random
import math
from enum import Enum

class Direction(Enum):
    North = 1
    East = 2
    South = 3
    West = 4


class Room:

    def __init__(self, index):
        self.index = index
        self.west = None
        self.east = None
        self.north = None
        self.south = None


class Dungeon:
    """Contains rooms for game stages."""
    current_room = None
    first_room = None

    def __init__(self, room_lim=10):
        self.room_count = 0
        self.first_room = Room(self.room_count)
        self.room_limit = room_lim
        self.current_room = self.first_room

    def generate_map(self):
        """Generates random dungeon maps."""
        while (self.room_count <= self.room_limit):
            self.room_count += 1
            self.random_integer = random.randint(1, 10)
            if(self.random_integer < 6):
                self.current_room.north = Room(self.room_count)
                self.current_room.north.south = self.current_room
                self.current_room = self.current_room.north
            elif(self.random_integer == 7 or self.random_integer == 8):
                self.current_room.west = Room(self.room_count)
                self.current_room.west.south = self.current_room
                self.current_room = self.current_room.west
            elif(self.random_integer == 9 or self.random_integer == 10):
                self.current_room.east = Room(self.room_count)
                self.current_room.east.south = self.current_room
                self.current_room = self.current_room.east

        self.current_room = self.first_room

    def next_room(self, direction):
        if(direction == Direction.North and self.current_room.north != None):
            self.current_room = self.current_room.north
        elif(direction == Direction.East and self.current_room.east != None):
            self.current_room = self.current_room.east
        elif(direction == Direction.South and self.current_room.south != None):
            self.current_room = self.current_room.south
        elif(direction == Direction.West and self.current_room.west != None):
            self.current_room = self.current_room.west
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
