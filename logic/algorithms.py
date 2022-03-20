from logic.ai import Data


def get_direction(start, destination):
    if destination[0] != start[0]:
        if destination[0] < start[0]:
            return "Left"
        return "Right"
    else:
        if destination[1] < start[1]:
            return "Up"
        return "Down"


def check_up(position, next):
    return next[0] == position[0] and next[1] < position[1]  # up


def check_down(position, next):
    return next[0] == position[0] and next[1] > position[1]  # down


def check_left(position, next):
    return next[0] < position[0] and next[1] == position[1]  # left


def check_right(position, next):
    return next[0] > position[0] and next[1] == position[1]  # right


def travel(graph, checktype, position):
    target = position
    has_next = False
    for next in graph[position]:
        if checktype(position, next):
            has_next = True
            target = next
    if has_next:
        return travel(graph, checktype, target)
    else:
        return target


def travel_a_star(graph, checktype, position, a_star_heuristic, nextQueue, counter):
    target = position
    has_next = False
    for n in graph[position]:
        if checktype(position, n):
            has_next = True
            target = n
            if a_star_heuristic.get(target) is None:
                a_star_heuristic[target] = counter
                nextQueue.append(target)
    if has_next:
        return travel_a_star(graph, checktype, target, a_star_heuristic, nextQueue, counter)
    else:
        return a_star_heuristic, nextQueue
