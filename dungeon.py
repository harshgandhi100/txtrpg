import random
import math

class room:
    room_count = 0
    def __init__(self):
        self.index = room_count
        self.left = None
        self.right = None
        self.front = None
        self.back = None
        room_count += 1
     
class dungeon:
    def __init__(self,n_rooms):
        self.numberOfRooms = n_rooms
        for i in range(numberOfRooms)
            self.rooms[i] = room()

    def join_rooms(self):
        for i in range(1,math.ceil(self.numberOfRooms/2)):
            self.rooms[i].front = i + 1
        for i in range(math.ceil(self.numberOfRooms/2)+1,self.numberOfRooms):
            while (self.chosen_room.left <> None or self.chosen_room.right <> None):
                self.chosen_room = self.rooms[random.randint(1,math.ceil(self.numberOfRooms/2))]
                if(self.chosen_room.left = None and self.chosen_room.right <> None):
                    self.chosen_room.left = self.rooms[i]
                elif (self.chosen_room.left <> None and self.chosen_room.right = None):
                    self.chosen_room.right = self.rooms[i]
                elif (self.chosen_room.left = None and self.chosen_room.right = None):
                    if(random.randint(0,1) = 0):
                        self.chosen_room.left = self.rooms[i]
                    else:
                        self.chosen_room.right = self.rooms[i]

