from copy import deepcopy

input_str = "..."

layout = [list(line) for line in input_str.split("\n")]

ROWS = len(layout)
COLS = len(layout[0])


directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]


def get_adjacent_occupied(state, x, y):
    n = 0
    for u, v in directions:
        p, q = x + u, y + v
        if 0 <= p < ROWS and 0 <= q < COLS:
            if state[p][q] == "#":
                n += 1
    return n


def get_next_state(state):
    next_state = deepcopy(state)
    for i in range(ROWS):
        for j in range(COLS):
            if state[i][j] == ".":
                continue
            adj_occupied = get_adjacent_occupied(state, i, j)
            if state[i][j] == "#" and adj_occupied >= 4:
                next_state[i][j] = "L"
            elif state[i][j] == "L" and adj_occupied == 0:
                next_state[i][j] = "#"
    return next_state


prev_state = layout
curr_state = get_next_state(prev_state)
while prev_state != curr_state:
    prev_state = curr_state
    curr_state = get_next_state(curr_state)

print(
    f"The number of occupied seats is: "
    + str(sum(sum(1 for s in line if s == "#") for line in curr_state))
)


# Part 2
def get_visible_occupied(state, x, y):
    n = 0
    for u, v in directions:
        i = 1
        p, q = x + i * u, y + i * v
        while 0 <= p < ROWS and 0 <= q < COLS and state[p][q] == ".":
            i += 1
            p, q = x + i * u, y + i * v
        if 0 <= p < ROWS and 0 <= q < COLS:
            if state[p][q] == "#":
                n += 1
    return n


def get_next_state(state):
    next_state = deepcopy(state)
    for i in range(ROWS):
        for j in range(COLS):
            if state[i][j] == ".":
                continue
            adj_occupied = get_visible_occupied(state, i, j)
            if state[i][j] == "#" and adj_occupied >= 5:
                next_state[i][j] = "L"
            elif state[i][j] == "L" and adj_occupied == 0:
                next_state[i][j] = "#"
    return next_state


prev_state = layout
curr_state = get_next_state(prev_state)
while prev_state != curr_state:
    prev_state = curr_state
    curr_state = get_next_state(prev_state)

print(
    f"The number of occupied seats is: "
    + str(sum(sum(1 for s in line if s == "#") for line in curr_state))
)

# Yeah, today's code is not that clean. But believe me, it was even worse before using
# the concept of 'direction' as a versor.
