# Adjascency List representation in Python
import pprint
from typing import Dict

from game.constants import COLS, ROWS


# Bi-Directional Adjacency List
class Graph(Dict):

    # Print the graph
    def print_graph(self):
        pprint.pprint(self)

    def add_edge(self, level, x, y):

        def add(source, destination):
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
            # Up
        def Up(level,x,y):
            if 0 < y and "S" not in level[y-1][x][:2]:
                add((x, y), (x, y-1))
            # Left
        def Left(level,x,y):
            if 0 < x and "E" not in level[y][x-1][:2]:
                add((x, y), (x-1, y))
            # Down
        def Down(level,x,y):
            if y < COLS - 1 and "N" not in level[y+1][x][:2]:
                add((x, y), (x, y+1))
            # Right
        def Right(level,x,y):
            if x < ROWS - 1 and "W" not in level[y][x+1][:2] :
                add((x, y), (x+1, y))
         
        if level[y][x][:2] == "C-": # Clear
            Up(level,x,y)
            Down(level,x,y)
            Left(level,x,y)
            Right(level,x,y)
        
        if level[y][x][:2] == "N-": # North
            Down(level,x,y)
            Left(level,x,y)
            Right(level,x,y)
        
        if level[y][x][:2] == "E-": # East
            Up(level,x,y)
            Down(level,x,y)
            Left(level,x,y)
          
        if level[y][x][:2] == "S-": # South
            Up(level,x,y)
            Left(level,x,y)
            Right(level,x,y)

        if level[y][x][:2] == "W-": # South
            Up(level,x,y)
            Down(level,x,y)
            Right(level,x,y)
        
        if level[y][x][:2] == "NE": # North East
            Down(level,x,y)
            Left(level,x,y)
        
        if level[y][x][:2] == "NW": # North West
            Down(level,x,y)
            Right(level,x,y)
        
        if level[y][x][:2] == "SE": # South East
            Up(level,x,y)
            Left(level,x,y)
        
        if level[y][x][:2] == "SW": # South West
            Up(level,x,y)
            Right(level,x,y)

    def remove_edge(self, source, destination):
        if destination in self[source]:
            self[source].remove(destination)
        if source in self[destination]:
            self[destination].remove(source)

        if len(self[source]) == 0:
            self.pop(source)

        if len(self[destination]) == 0:
            self.pop(destination)
