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

    state_cost = dict()


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

   
def setActiveRobot(token_color):
    if token_color[0] == "R":
        Data.activeRobot = 0
    if token_color[0] == "B":
        Data.activeRobot = 1
    if token_color[0] == "G":
        Data.activeRobot = 2
    if token_color[0] == "Y":
        Data.activeRobot = 3


def ConstructGUIPath(finalPath):
    moves = []
    for i, j in enumerate(finalPath[:-1]):
        for k in range(0, 4):
            if j[k] != finalPath[i + 1][k]:
                moves.append((k, datastructures.get_direction(j[k], finalPath[i + 1][k])))
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


def state_already_visited_a_star(state):

    if Data.parentMap.get(state) is not None:
        return True

    # temp = list(state)
    # active_robot_location = state[Data.activeRobot]
    # del temp[Data.activeRobot]
    #
    # state_permutations = list(itertools.permutations(temp))
    #
    # for perm in state_permutations:
    #     a = list(perm)
    #     insert_at = Data.activeRobot
    #     b = a[:]
    #     b[insert_at:insert_at] = [active_robot_location]
    #     if Data.parentMap.get(tuple(b)) is not None:
    #         return True

def BFS(graph):
    start = time.time()
    pathFound = False
    endState = None
    finalPath = []
    queue = []
    amount_of_states_considered = 0
    Data.aiGraph = datastructures.optimize_adjacency_list(graph)
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


def a_star(graph):
    start = time.time()
    pathFound = False
    endState = None
    finalPath = []
    queue = []
    amount_of_states_considered = 0
    Data.aiGraph = datastructures.optimize_adjacency_list(graph)
    heuristic = datastructures.get_astar_heuristic_dict(graph, Data.activeToken)
    queue.append((Data.startState, 0))
    Data.parentMap[Data.startState] = None

    while len(queue) != 0 and pathFound is False:
        currentState = queue.pop(0)[0]
        # print(currentState)
        legalNewStates = GetLegalMoves(currentState, Data.parentMap.get(currentState))
        amount_of_states_considered += len(legalNewStates)
        for state in legalNewStates:
            cost = -1
            if state_already_visited_a_star(state):
                cost = heuristic.get(state[Data.activeRobot]) + get_depth(currentState)
                if cost >= Data.state_cost.get(state):
                    continue

            if cost == -1:
                cost = heuristic.get(state[Data.activeRobot]) + get_depth(currentState)
            Data.parentMap[state] = currentState

            Data.state_cost[state] = cost
            pathFound = GoalTest(state)
            # print(" Testing ", state)

            if pathFound:
                 endState = state
                 end = time.time()
                 print("Found goal state with ", amount_of_states_considered, " states considered")
                 print("Time elapsed:", end - start, "seconds")
                 break

            if len(queue) == 0:
                queue.insert(0, (state, cost))
            else:
                index = binary_search_recursive(queue, cost, 0, len(queue))
                queue.insert(index, (state, cost))

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

def get_depth(state):
    counter = 0
    currentState = state
    while Data.parentMap.get(currentState) is not None:
        counter += 1
        currentState = Data.parentMap.get(currentState)
        if counter > 14:
            i=1
    return counter

def binary_search_recursive(array, element, start, end):
    if start > end:
        return start

    if start == end:
        return start

    mid = (start + end) // 2
    if element == array[mid][1]:
        return mid

    if element < array[mid][1]:
        return binary_search_recursive(array, element, start, mid-1)
    else:
        return binary_search_recursive(array, element, mid+1, end)

def solve(algorithm, graph, players, token_color, goal):
    if len(players) == 4:
        temp = []
        for player in players:
            temp.append(player.position)
        Data.startState = tuple(temp)
        Data.activeToken = goal
        setActiveRobot(token_color)
        Data.parentMap.clear()

    if algorithm == "BFS":
        print("BFS")
        return BFS(graph)

        # return BFS()
    if algorithm == "a_star":
        print("a_star")
        return a_star(graph)
