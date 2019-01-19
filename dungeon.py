import random
import math

class room:
    room_count = 0
    def __init__(self):
        self.index = room_count
        self.links = [None] * 4
    
class dungeon:
    def __init__(self,n_rooms):
        
