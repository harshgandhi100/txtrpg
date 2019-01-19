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
    current_room = None
    first_room = None
    def __init__(self,room_lim = 10):
        self.first_room = Room()
        self.room_limit = room_lim
        self.current_room = self.first_room


    def generate_map(self):
        while (Room.room_count <= self.room_limit):
            self.current_room.front = Room()
            self.current_room = self.current_room.front
        self.current_room = self.first_room

    def next_room(self):
        self.current_room = self.current_room.front

def main():
    d = Dungeon()
    d.generate_map()
    while(d.current_room.front is not None):
        print(d.current_room.index)
        d.next_room()
if __name__ == "__main__":
    main()
