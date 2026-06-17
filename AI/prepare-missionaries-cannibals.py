from collections import deque


START = (3, 3, 1)
GOAL = (0, 0, 0)


def is_valid(state):
    m_left, c_left, _ = state
    m_right = 3 - m_left
    c_right = 3 - c_left

    if not (0 <= m_left <= 3 and 0 <= c_left <= 3):
        return False

    if m_left > 0 and m_left < c_left:
        return False

    if m_right > 0 and m_right < c_right:
        return False

    return True


def get_children(state):
    children = []
    m_left, c_left, boat = state

    moves = [
        (1, 0),
        (2, 0),
        (0, 1),
        (0, 2),
        (1, 1),
    ]

    for move_m, move_c in moves:
        if boat == 1:
            child = (m_left - move_m, c_left - move_c, 0)
        else:
            child = (m_left + move_m, c_left + move_c, 1)

        if is_valid(child):
            children.append(child)

    return children


def heuristic(state):
    # Uoc luong don gian: con bao nhieu nguoi o ben trai.
    m_left, c_left, _ = state
    return m_left + c_left


def build_graph(start=START):
    graph = {}
    weighted_graph = {}
    heuristic_table = {}

    queue = deque([start])
    visited = {start}

    while queue:
        state = queue.popleft()
        children = get_children(state)

        graph[state] = children
        weighted_graph[state] = [(child, 1) for child in children]
        heuristic_table[state] = heuristic(state)

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
    for step, item in enumerate(path):
        if isinstance(item, tuple) and len(item) == 2 and isinstance(item[0], tuple):
            state, action = item
            print(f"Buoc {step}: state = {state}, action = {action}")
        else:
            print(f"Buoc {step}: {item}")

    print("Tong chi phi:", total_cost)


if __name__ == "__main__":
    graph, weighted_graph, heuristic_table, start, goals = build_graph()

    print("Start:", start)
    print("Goal:", GOAL)
    print("So trang thai:", len(graph))
    print("Cac trang thai ke cua start:", graph[start])
    print("Heuristic cua start:", heuristic_table[start])
