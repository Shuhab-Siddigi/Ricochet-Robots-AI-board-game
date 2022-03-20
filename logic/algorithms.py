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
