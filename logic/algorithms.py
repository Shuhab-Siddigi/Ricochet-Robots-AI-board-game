visited = set()  # Set to keep track of visited nodes.

aiGraph = {}

startState = ((0, 0), (5, 9), (3, 5), (13, 13))


def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


def getDirection(start, destination):
    if destination.x != start.x:
        if destination.x < start.x:
            return "Left"
        return "Right"
    else:
        if destination.y < start.y:
            return "Up"
        return "Down"


def GetLegalMoves(state, parentState=None):  # TODO Make logic to ignore previously visited states.
    moves = {}
    legalNewStates = []

    for p in state:
        moves[p] = []

    for currentPlayer in state:
        for otherPlayer in state:
            if otherPlayer != currentPlayer:
                adjacencyMoves = aiGraph[currentPlayer]
                for move in adjacencyMoves:
                    if currentPlayer.x != otherPlayer.x and currentPlayer.y != otherPlayer.y:
                        moves[currentPlayer].append(move)
                        break
                    elif currentPlayer.x > otherPlayer.x >= move.x:
                        moves[currentPlayer].append((otherPlayer.x + 1, otherPlayer.y))
                    elif currentPlayer.x < otherPlayer.x <= move.x:
                        moves[currentPlayer].append((otherPlayer.x - 1, otherPlayer.y))
                    elif currentPlayer.y > otherPlayer.y >= move.y:
                        moves[currentPlayer].append((otherPlayer.x, otherPlayer.y + 1))
                    elif currentPlayer.y < otherPlayer.y <= move.y:
                        moves[currentPlayer].append((otherPlayer.x, otherPlayer.y - 1))
                    else:
                        moves[currentPlayer].append(move)

    for index, p in enumerate(state):
        for coord in moves[p]:
            temp = list(state)
            temp[index] = coord
            if tuple(temp) != parentState:  # Removes parent-state as a legal move to avoid going back and forward
                legalNewStates.append(tuple(temp))
    return legalNewStates


def GoalTest(move):  # TODO
    pass


def ConstructGUIPath(finalPath):  # TODO
    moves = []
    # [(1, 1)] =humanReadable= [(player1, "left")] Sort start -> end
    return moves


def BFS():
    parentMap = dict()
    pathFound = False
    endState = None
    finalPath = []
    queue = GetLegalMoves(startState)
    parentMap[startState] = None
    while len(queue) != 0 and pathFound is False:
        currentState = queue.pop()
        if parentMap.get(currentState) is not None:
            legalNewStates = GetLegalMoves(currentState, parentMap.get(currentState))
            for state in legalNewStates:
                pathFound = GoalTest(state)
                parentMap[state] = currentState
                if (pathFound):
                    endState = state
                    break
                queue.append(state)
    finalPath.append(endState)
    currentState = endState
    while parentMap.get(currentState) != None:
        currentState = parentMap.get(currentState)
        finalPath.insert(0, currentState)  # Is same as prepend

    return ConstructGUIPath(finalPath)


def solve(algorithm):
    if algorithm == "BFS":
        print("BFS")
        # return BFS()
    if algorithm == "AStar":
        print("AStar")
        # return AStar()
