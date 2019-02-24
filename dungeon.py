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
    map = [None]

    def __init__(self, room_lim=10):
        self.room_count = 0
        self.branches = []
        self.first_room = Room(self.room_count)
        self.room_limit = room_lim
        self.current_room = self.first_room
        self.branches.append(self.current_room)
            
    def generate_map(self):
        """Generates random dungeon maps."""
        while (self.room_count < self.room_limit):
            self.room_count += 1

            if (self.room_count <= self.room_limit/2):
                Dungeon.map.append(Direction.North.value)
                self.branches.append([self.current_room])
                self.current_room.north = Room(self.room_count)
                self.current_room.north.south = self.current_room
                self.current_room = self.current_room.north
            else:
                flag = False


                while (flag == False):
                    self.random_integer = random.randint(1, self.room_limit/2)
                    current_branch = self.branches[random_integer-1]
                    room_list = getAvailableRooms(self.branches[random_integer-1])
                    if(len(room_list)>0):
                        
                    

                    


                # self.random_integer = random.randint(1, 4)
                # if(self.random_integer <= 6):
                #     Dungeon.map.append(Direction.North.value)
                #     self.current_room.north = Room(self.room_count)
                #     self.current_room.north.south = self.current_room
                #     self.current_room = self.current_room.north
                # elif(self.random_integer == 7 or self.random_integer == 8):
                #     Dungeon.map.append(Direction.West.value)
                #     self.current_room.west = Room(self.room_count)
                #     self.current_room.west.east = self.current_room
                #     self.current_room = self.current_room.west
                # elif(self.random_integer == 9 or self.random_integer == 10):
                #     Dungeon.map.append(Direction.East.value)
                #     self.current_room.east = Room(self.room_count)
                #     self.current_room.east.west = self.current_room
                #     self.current_room = self.current_room.east

        self.current_room = self.first_room

    
    def next_room(self, direction):
        if(direction == Direction.North.value and self.current_room.north != None):
            self.current_room = self.current_room.north
        elif(direction == Direction.East.value and self.current_room.east != None):
            self.current_room = self.current_room.east
        elif(direction == Direction.South.value and self.current_room.south != None):
            self.current_room = self.current_room.south
        elif(direction == Direction.West.value and self.current_room.west != None):
            self.current_room = self.current_room.west
        else:
            self.current_room = self.current_room

def getAvailableDirections(room: Room):
    availableDirections = []
    if(room.east == None) :
        availableDirections.append(Direction.East)
    elif(room.west == None) :
        availableDirections.append(Direction.West)
    elif(room.north == None) :
        availableDirections.append(Direction.North)
    elif(room.south == None) :
        availableDirections.append(Direction.South)
    return availableDirections

def getAvailableRooms(roomlist: list):
    availableRooms = []
    for room in roomlist:
        if(getAvailableDirections(room).count() > 0):
            availableRooms.append(room)
    return availableRooms

def main():
    d = Dungeon()
    d.generate_map()
    inp = None
    print(Dungeon.map)
    while(inp != 0):
        print("Current Room: " + str(d.current_room.index))
        inp = int(input())
        d.next_room(inp)
   

if __name__ == "__main__":
    main()
