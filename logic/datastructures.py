# Adjascency List representation in Python
import pprint
from typing import Dict
import copy

from game.constants import COLS, ROWS
from logic.algorithms import *


class Graph(Dict):

    # Print the graph
    def print_graph(self):
        pprint.pprint(self)

    def add_bidirectional(self, source, destination):
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

    def add(self, source, destination):
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
        def Up(level, x, y):
            if 0 < y and "S" not in level[y - 1][x][:2]:
                self.add_bidirectional((x, y), (x, y - 1))
            # Left
        def Left(level, x, y):
            if 0 < x and "E" not in level[y][x - 1][:2]:
                self.add_bidirectional((x, y), (x - 1, y))
            # Down
        def Down(level, x, y):
            if y < COLS - 1 and "N" not in level[y + 1][x][:2]:
                self.add_bidirectional((x, y), (x, y + 1))
            # Right
        def Right(level, x, y):
            if x < ROWS - 1 and "W" not in level[y][x + 1][:2]:
                self.add_bidirectional((x, y), (x + 1, y))

        if level[y][x][:2] == "C-":  # Clear
            Up(level, x, y)
            Down(level, x, y)
            Left(level, x, y)
            Right(level, x, y)

        if level[y][x][:2] == "N-":  # North
            Down(level, x, y)
            Left(level, x, y)
            Right(level, x, y)

        if level[y][x][:2] == "E-":  # East
            Up(level, x, y)
            Down(level, x, y)
            Left(level, x, y)

        if level[y][x][:2] == "S-":  # South
            Up(level, x, y)
            Left(level, x, y)
            Right(level, x, y)

        if level[y][x][:2] == "W-":  # South
            Up(level, x, y)
            Down(level, x, y)
            Right(level, x, y)

        if level[y][x][:2] == "NE":  # North East
            Down(level, x, y)
            Left(level, x, y)

        if level[y][x][:2] == "NW":  # North West
            Down(level, x, y)
            Right(level, x, y)

        if level[y][x][:2] == "SE":  # South East
            Up(level, x, y)
            Left(level, x, y)

        if level[y][x][:2] == "SW":  # South West
            Up(level, x, y)
            Right(level, x, y)


def optimize_adjacency_list(graph):
    g = copy.deepcopy(graph)
    optimized_graph = Graph()
    for key in g.keys():
        if travel(g, check_left, key) != key:
            optimized_graph.add(key, travel(g, check_left, key))
        if travel(g, check_right, key) != key:
            optimized_graph.add(key, travel(g, check_right, key))
        if travel(g, check_up, key) != key:
            optimized_graph.add(key, travel(g, check_up, key))
        if travel(g, check_down, key) != key:
            optimized_graph.add(key, travel(g, check_down, key))

    return optimized_graph


def get_astar_heuristic_dict(graph, goal):
    g = copy.deepcopy(graph)

    a_star_heuristic = {}
    queue = []
    nextQueue = []
    counter = 0
    queue.append(goal)
    a_star_heuristic[goal] = 0

    while len(queue) != 0:
        for position in queue:
            a_star_heuristic, nextQueue = \
                travel_a_star(g, check_left, position, a_star_heuristic, nextQueue, counter+1)
            a_star_heuristic, nextQueue = \
                travel_a_star(g, check_right, position, a_star_heuristic, nextQueue, counter+1)
            a_star_heuristic, nextQueue = \
                travel_a_star(g, check_up, position, a_star_heuristic, nextQueue, counter+1)
            a_star_heuristic, nextQueue = \
                travel_a_star(g, check_down, position, a_star_heuristic, nextQueue, counter+1)
        queue.clear()
        for x in nextQueue:
            queue.append(x)
        nextQueue.clear()
        counter += 1

    return a_star_heuristic
