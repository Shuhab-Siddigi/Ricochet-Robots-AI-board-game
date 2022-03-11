# Adjascency List representation in Python
import pprint
from typing import Dict

from game.constants import COLS, ROWS

# Bi-Directional Adjacencylist
class Graph(Dict):

    # Print the graph
    def print_graph(self):
      pprint.pprint(self)
    
    def add_edge(self,level,x,y):
        
        def add(source,destination):
                    # -> Direction
            if source not in self:
                self[source] = []
            if destination not in self[source]: 
                self[source].append(destination)
            
            # <- Direction
            if destination not in self:
                self[destination] = []
            if source not in self[destination]:
                self[destination].append(source)

        if x < ROWS-1:
            if level[y][x+1][:2] == "C-": # Right
                add((x,y),(x+1,y))
            if level[y][x+1][:2] == "NE": # North East (right)
                add((x,y),(x+1,y))
            if level[y][x+1][:2] == "E-": # East
                add((x,y),(x+1,y))
            if level[y][x+1][:2] == "SE": # South East (right)
                add((x,y),(x+1,y))
        
        if y < COLS-1:
            if level[y+1][x][:2] == "C-": # Down
                add((x,y),(x,y+1))
            if level[y+1][x][:2] == "S-": # South
                add((x,y),(x,y+1))
            if level[y+1][x][:2] == "SE": # South East (down)
                add((x,y),(x,y+1))
            if level[y+1][x][:2] == "SW":  # South West (down)
                add((x,y),(x,y+1))     
        
        if 0 < x:
            if level[y][x-1][:2] == "C-": # Left
                add((x,y),(x-1,y))
            if level[y][x-1][:2] == "W-": # West
                add((x,y),(x-1,y))
            if level[y][x-1][:2] == "NW": # North West (left)
                add((x,y),(x-1,y))
            if level[y][x-1][:2] == "SW":  # South West (left)
                add((x,y),(x-1,y))   
        
        if 0 < y:
            if level[y-1][x][:2] == "C-": # Up
                add((x,y),(x,y-1))
            if level[y-1][x][:2] == "N-": # North
                add((x,y),(x,y-1))
            if level[y-1][x][:2] == "NW": # North West (up)
                add((x,y),(x,y-1))
            if level[y-1][x][:2] == "NE": # North East (up)
                add((x,y),(x,y-1))
                
    
    def remove_edge(self,source,destination):
        if destination in self[source]:
            self[source].remove(destination)
        if source in self[destination]:
            self[destination].remove(source)
        
        if len(self[source]) == 0:
            self.pop(source)

        if len(self[destination]) == 0:
            self.pop(destination)