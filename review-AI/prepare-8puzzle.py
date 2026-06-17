from collections import deque

START = (1, 2, 3, 4, 5, 6, 0, 7, 8)
GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def get_child(state):
    child = []
    zero_index = state.index(0)
    row, col = divmod(zero_index, 3)

    moves = [(0, 1), (-1, 0), (1, 0), (0, -1)]


    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_col < 3 and 0 <= new_row < 3:
            new_index = new_row * 3 + new_col
            new_state = list(state)
            new_state[zero_index], new_state[new_index] = (
                new_state[new_index], new_state[zero_index]
            )
            child.append(tuple(new_state))
        
    return child

def h1(state):
    count = 0

    for i in range(0, 9):
        if state[i] != 0 and state[i] != GOAL[i]:
            count += 1
    return count

def h2(state):
    total = 0

    for i, v in enumerate(state):
        row, col = state(i)
        goal_index = GOAL.index(v)
        goal_row, goal_col = state(goal_index)

        total += abs(row - goal_row) + abs(col - goal_col)
    return total

def build_graph(start= START, h_type= "h2"):
    graph = {}
    w_graph = {}
    h_table = {}
    h_func = h1 if h_type== "h1" else h2

    queue = deque([start])
    visited = {start}

    while queue:
        state = queue.popleft()
        child = get_child(state)

        graph[state] = child
        w_graph[state] = [(c, 1) for c in child]
        h_table[state] = h_func(state)

        for c in child:
            if c not in visited:
                visited.add(c)
                queue.append(c)

    return graph, w_graph, h_table, start, {GOAL}

def print_path(path, total_cost= None):
    if path is None:
        print("khong tim thay duong di")
        return
    if total_cost is None:
        total_cost = len(path) - 1

    for step, state in enumerate(path):
        print(f'Step {step}:')
        print_state(state)

def print_state(state):
    for i in range(0, 9, 3):
        row = state[i, i + 3]
        print(" ".join("_" if x == 0 else str(x) for x in row))

