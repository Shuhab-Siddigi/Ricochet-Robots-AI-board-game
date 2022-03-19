import itertools
import pprint
import time

from logic import datastructures


class Data:
    aiGraph = None
    startState = ((0, 0), (5, 9), (3, 5), (13, 13))

    activeRobot = None
    activeToken = None

    parentMap = dict()


def GetLegalMoves(state, parentState=None):
    moves = {}
    legalNewStates = []

    for p in state:
        moves[p] = []

    for currentPlayer in state:
        adjacencyMoves = Data.aiGraph[currentPlayer]
        for move in adjacencyMoves:
            moves[currentPlayer].append(adjust_move_for_robots(state, currentPlayer, move))

    for index, p in enumerate(state):
        for coord in moves[p]:
            temp = list(state)
            temp[index] = coord
            if tuple(temp) != parentState and tuple(
                    temp) != Data.startState:  # Removes parent-state as a legal move to avoid going back and forward
                legalNewStates.append(tuple(temp))
    return legalNewStates


def adjust_move_for_robots(state, current_player, move):
    temp = None

    for otherPlayer in state:
        if otherPlayer != current_player:

            if current_player[0] != otherPlayer[0] and current_player[1] != otherPlayer[1]:
                continue

            elif current_player[0] > otherPlayer[0] >= move[0]:  # Robot at left
                if temp is not None:
                    if current_player[0] > otherPlayer[0] >= temp[0]:
                        temp = (otherPlayer[0] + 1, otherPlayer[1])
                else:
                    temp = (otherPlayer[0] + 1, otherPlayer[1])

            elif current_player[0] < otherPlayer[0] <= move[0]:  # Robot at right
                if temp is not None:
                    if current_player[0] < otherPlayer[0] <= temp[0]:
                        temp = (otherPlayer[0] - 1, otherPlayer[1])
                else:
                    temp = (otherPlayer[0] - 1, otherPlayer[1])

            elif current_player[1] > otherPlayer[1] >= move[1]:  # Robot at down
                if temp is not None:
                    if current_player[1] > otherPlayer[1] >= temp[1]:
                        temp = (otherPlayer[0], otherPlayer[1] + 1)
                else:
                    temp = (otherPlayer[0], otherPlayer[1] + 1)

            elif current_player[1] < otherPlayer[1] <= move[1]:  # Robot at up
                if temp is not None:
                    if current_player[1] < otherPlayer[1] <= temp[1]:
                        temp = (otherPlayer[0], otherPlayer[1] - 1)
                else:
                    temp = (otherPlayer[0], otherPlayer[1] - 1)
    if temp is None:
        temp = move

    return temp


def GoalTest(state):
    return state[Data.activeRobot] == Data.activeToken


def setActiveRobot():
    Data.activeRobot = 0


def ConstructGUIPath(finalPath):
    moves = []
    for i, j in enumerate(finalPath[:-1]):
        for k in range(0, 4):
            if j[k] != finalPath[i + 1][k]:
                moves.append((k, datastructures.get_direction(j[k], finalPath[i + 1][k])))

    # # [(1, 1)] =humanReadable= [(player1, "left")] Sort start -> end
    #up, down, left, right

    return moves


def stateAlreadyExplored(state):
    if Data.parentMap.get(state) is not None:
        return True

    temp = list(state)
    active_robot_location = state[Data.activeRobot]
    del temp[Data.activeRobot]

    state_permutations = list(itertools.permutations(temp))

    for perm in state_permutations:
        a = list(perm)
        insert_at = Data.activeRobot
        b = a[:]
        b[insert_at:insert_at] = [active_robot_location]
        if Data.parentMap.get(tuple(b)) is not None:
            return True


def BFS(graph):
    start = time.time()
    pathFound = False
    endState = None
    finalPath = []
    queue = []
    amount_of_states_considered = 0
    Data.aiGraph = datastructures.optimize_adjacency_list(graph)
    setActiveRobot()
    queue.append(Data.startState)
    Data.parentMap[Data.startState] = None

    while len(queue) != 0 and pathFound is False:
        currentState = queue.pop(0)
        legalNewStates = GetLegalMoves(currentState, Data.parentMap.get(currentState))
        amount_of_states_considered += len(legalNewStates)
        for state in legalNewStates:
            if stateAlreadyExplored(state):
                continue
            pathFound = GoalTest(state)
            # print(" Testing ", state)
            Data.parentMap[state] = currentState
            if (pathFound):
                endState = state
                end = time.time()
                print("Found goal state with ", amount_of_states_considered, " states considered")
                print("Time elapsed:", end - start, "seconds")
                break
            queue.append(state)

    finalPath.append(endState)
    currentState = endState

    while Data.parentMap.get(currentState) is not None:
        currentState = Data.parentMap.get(currentState)
        finalPath.insert(0, currentState)  # Is same as prepend

    print("Found solution in ", len(finalPath) - 1)
    print("\n Path: \n")
    pprint.pprint(finalPath)
    print(ConstructGUIPath(finalPath))
    return ConstructGUIPath(finalPath)


def solve(algorithm, graph, players, goal):
    if len(players) == 4:
        temp = []
        for player in players:
            temp.append(player.position)
        Data.startState = tuple(temp)
        Data.activeToken = goal

    if algorithm == "BFS":
        print("BFS")
        return BFS(graph)

        # return BFS()
    if algorithm == "AStar":
        print("AStar")
        # return AStar()