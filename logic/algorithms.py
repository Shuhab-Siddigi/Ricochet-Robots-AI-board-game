
import pprint
from logic import datastructures


visited = set()  # Set to keep track of visited nodes.

# aiGraph = None
# startState = ((0, 0), (5, 9), (3, 5), (13, 13))


# activeRobot = None
# activeToken = ((3,6),0)



def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

class Data:

    aiGraph = None
    startState = ((0, 0), (5, 9), (3, 5), (13, 13))


    activeRobot = None
    activeToken = ((0,15),0)

def GetLegalMoves(state, parentState=None):  # TODO Make logic to ignore previously visited states.
    moves = {}
    legalNewStates = []

    for p in state:
        moves[p] = []

    for currentPlayer in state:
        adjacencyMoves = Data.aiGraph[currentPlayer]
        for move in adjacencyMoves:
            moves[currentPlayer].append(adjust_move_for_robots(state,currentPlayer, move))
  
    for index, p in enumerate(state):
        for coord in moves[p]:
            temp = list(state)
            temp[index] = coord
            # print(tuple(temp) != parentState)
            if tuple(temp) != parentState and tuple(temp) != Data.startState:  # Removes parent-state as a legal move to avoid going back and forward
                legalNewStates.append(tuple(temp))
    return legalNewStates


def adjust_move_for_robots(state, current_player, move): 
    temp = None

    for otherPlayer in state:
        if otherPlayer != current_player:

            if current_player[0] != otherPlayer[0] and current_player[1] != otherPlayer[1]:
                continue

            elif current_player[0] > otherPlayer[0] >= move[0]: # Robot at left
                if temp is not None:
                    if current_player[0] > otherPlayer[0] >= temp[0]:
                        temp = (otherPlayer[0] + 1, otherPlayer[1])
                else: 
                    temp = (otherPlayer[0] + 1, otherPlayer[1])

            elif current_player[0] < otherPlayer[0] <= move[0]: # Robot at right
                if temp is not None:
                    if current_player[0] < otherPlayer[0] <= temp[0]:
                        temp = (otherPlayer[0] - 1, otherPlayer[1])
                else: 
                    temp = (otherPlayer[0] - 1, otherPlayer[1])

            elif current_player[1] > otherPlayer[1] >= move[1]: # Robot at down
                if temp is not None:
                    if current_player[1] > otherPlayer[1] >= temp[1]:
                        temp = (otherPlayer[0], otherPlayer[1] + 1)
                else: 
                    temp = (otherPlayer[0], otherPlayer[1] + 1)

            elif current_player[1] < otherPlayer[1] <= move[1]: # Robot at up
                if temp is not None:
                    if current_player[1] < otherPlayer[1] <= temp[1]:
                        temp = (otherPlayer[0], otherPlayer[1] - 1)
                else: 
                    temp = (otherPlayer[0], otherPlayer[1] - 1)
    if temp is None:
        temp = move

    return temp




def GoalTest(state):  # TODO
    return state[Data.activeRobot] == Data.activeToken[0]

def setActiveRobot():
    Data.activeRobot = 0

def ConstructGUIPath(finalPath):  # TODO
    moves = []
    # [(1, 1)] =humanReadable= [(player1, "left")] Sort start -> end
    return moves


def BFS(graph):
    parentMap = dict()
    pathFound = False
    endState = None
    finalPath = []
    queue = []
    Data.aiGraph = datastructures.optimize_adjacency_list(graph)
    setActiveRobot()
    # queue = GetLegalMoves(Data.startState)
    queue.append(Data.startState)

    # print(queue)
    # print(len(queue))
    parentMap[Data.startState] = None

    while len(queue) != 0 and pathFound is False:
        currentState = queue.pop(0)
        # print(parentMap.get(currentState))

        legalNewStates = GetLegalMoves(currentState, parentMap.get(currentState))
        for state in legalNewStates:
            if parentMap.get(state) is not None:
                continue
            pathFound = GoalTest(state)
            # print(" Testing ", state)
            parentMap[state] = currentState
            if (pathFound):
                endState = state
                print(endState)
                print("Found token with ", len(queue), " states")
                break
            queue.append(state)

    # parentMap[Data.startState] = None

    finalPath.append(endState)
    currentState = endState
    # pprint.pprint(parentMap)
    while parentMap.get(currentState) != None:
        # print(len(parentMap.get(currentState)) > 1)
        currentState1 = parentMap.get(currentState)
        # print(currentState1)
        finalPath.insert(0,currentState1)  # Is same as prepend
        
        currentState = currentState1

    print("Found solution in " ,len(finalPath) -1)
    print("\n Path: \n", finalPath)

    return finalPath
    # return ConstructGUIPath(finalPath)


def solve(algorithm, graph):
    if algorithm == "BFS":
        print("BFS")
        BFS(graph)
    
        # return BFS()
    if algorithm == "AStar":
        print("AStar")
        # return AStar()
