# Adjascency List representation in Python
import pprint
from typing import Dict
import copy

from game.constants import COLS, ROWS
class Graph(Dict):

    # Print the graph
    def print_graph(self):
        pprint.pprint(self)

    def add_bidirectional(self,source, destination):
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

    def add(self,source, destination):
        # -> Direction
        if source not in self:
            self[source] = []
        if destination not in self[source]:
            self[source].append(destination)


    def remove(self, source, destination):
        if destination in self[source]:
            self[source].remove(destination)
        if source in self[destination]:
            self[destination].remove(source)

        if len(self[source]) == 0:
            self.pop(source)

        if len(self[destination]) == 0:
            self.pop(destination)

# Bi-Directional Adjacency List
class Board_graph(Graph):

    # Print the graph
    def print_graph(self):
        pprint.pprint(self)

    def add_edge(self, level, x, y):
            # Up
        def Up(level,x,y):
            if 0 < y and "S" not in level[y-1][x][:2]:
                self.add_bidirectional((x, y), (x, y-1))
            # Left
        def Left(level,x,y):
            if 0 < x and "E" not in level[y][x-1][:2]:
                self.add_bidirectional((x, y), (x-1, y))
            # Down
        def Down(level,x,y):
            if y < COLS - 1 and "N" not in level[y+1][x][:2]:
                self.add_bidirectional((x, y), (x, y+1))
            # Right
        def Right(level,x,y):
            if x < ROWS - 1 and "W" not in level[y][x+1][:2] :
                self.add_bidirectional((x, y), (x+1, y))
         
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


def get_direction(start, destination):
    if destination[0] != start[0]:
        if destination[0] < start[0]:
            return "Left"
        return "Right"
    else:
        if destination[1] < start[1]:
            return "Up"
        return "Down"


def travel(graph,checktype,position):
    target = position
    has_next = False
    for next in graph[position]:
        if checktype(position,next):
            has_next = True
            target = next
    if has_next:
        return travel(graph,checktype,target)
    else:
        return target

def optimize_adjacency_list(graph):
    g = copy.deepcopy(graph)
    optimized_graph = Graph()
    for key in g.keys():
        # for neighbour in g[key]:
    
        # if(self.get_direction(key, neighbour) == "Left"):
        optimized_graph.add(key, travel(g, check_left, key))
        # if(get_direction(key, neighbour) == "Right"):
        optimized_graph.add(key, travel(g, check_right, key))
        # if(get_direction(key, neighbour) == "Up"):
        optimized_graph.add(key, travel(g, check_up, key))
        # if(get_direction(key, neighbour) == "Down"):
        optimized_graph.add(key, travel(g, check_down, key))

    pprint.pprint(optimized_graph)

    return optimized_graph


def check_up(position, next):
    return next[0] == position[0] and next[1] < position[1] # up
def check_down(position,next):
    return next[0] == position[0] and next[1] > position[1] # down
def check_left(position,next):
    return next[0] < position[0] and next[1] == position[1] # left
def check_right(position,next):
    return next[0] > position[0] and next[1] == position[1] # right