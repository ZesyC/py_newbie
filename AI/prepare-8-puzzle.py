from collections import deque


START = (1, 2, 3, 4, 5, 6, 0, 7, 8)
GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)


def get_children(state):
    children = []
    zero_index = state.index(0)
    row, col = divmod(zero_index, 3)

    moves = [(0, 1), (-1, 0), (1, 0), (0, -1)]

    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_index = new_row * 3 + new_col
            new_state = list(state)
            new_state[zero_index], new_state[new_index] = (
                new_state[new_index],
                new_state[zero_index],
            )
            children.append(tuple(new_state))

    return children


def h1(state):
    # h1: dem so o sai vi tri, khong tinh o trong 0.
    count = 0

    for i in range(9):
        if state[i] != 0 and state[i] != GOAL[i]:
            count += 1

    return count


def h2(state):
    # h2: Manhattan distance, tong khoang cach moi o so ve dung vi tri dich.
    total = 0

    for index, value in enumerate(state):
        if value == 0:
            continue

        current_row, current_col = divmod(index, 3)
        goal_index = GOAL.index(value)
        goal_row, goal_col = divmod(goal_index, 3)

        total += abs(current_row - goal_row) + abs(current_col - goal_col)

    return total


def build_graph(start=START, heuristic_type="h2"):
    graph = {}
    weighted_graph = {}
    heuristic_table = {}
    heuristic_func = h1 if heuristic_type == "h1" else h2

    queue = deque([start])
    visited = {start}

    while queue:
        state = queue.popleft()
        children = get_children(state)

        graph[state] = children
        weighted_graph[state] = [(child, 1) for child in children]
        heuristic_table[state] = heuristic_func(state)

        for child in children:
            if child not in visited:
                visited.add(child)
                queue.append(child)

    return graph, weighted_graph, heuristic_table, start, {GOAL}


def print_path_result(path, total_cost=None):
    if path is None:
        print("Khong tim thay duong di.")
        return

    if total_cost is None:
        total_cost = len(path) - 1

    print("Duong di:")
    for step, state in enumerate(path):
        print(f"\nBuoc {step}:")
        print_state(state)

    print("\nTong chi phi:", total_cost)


def print_state(state):
    for i in range(0, 9, 3):
        row = state[i:i + 3]
        print(" ".join("_" if x == 0 else str(x) for x in row))


if __name__ == "__main__":
    graph, weighted_graph, heuristic_table, start, goals = build_graph()

    print("Start:")
    print_state(start)

    print("\nGoal:")
    print_state(GOAL)

    print("\nSo trang thai:", len(graph))
    print("h1 cua start:", h1(start))
    print("h2 cua start:", h2(start))
