import random
import math

class Adjnode:
    def __init__(self,data):
        self.roomId = data
        self.link = None

class Dungeon:
    def __init__(self,n_rooms):
        self.numberOfRooms = n_rooms
        self.layout = [None] * numberOfRooms

    def add_doors_between(self,source,destination):
        connection = Adjnode(destination)
        connection.link = self.layout[source]
        self.layout[source] = connection

        connection = Adjnode(source)
        connection.link = self.layout[destination]
        self.layout[destination] = connection

    def next_room()
    