import random
import math

class Node:
    def __init__(self,data):
        self.roomId = data
        self.link = None

class Dungeon:
    def __init__(self,n_rooms):
        self.numberOfRooms = n_rooms
        self.layout = [None] * numberOfRooms

    def add_doors_between(self,source,destination):
        