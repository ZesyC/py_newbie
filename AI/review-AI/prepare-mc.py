from collections import deque


START = (3, 3, 1)
GOAL = (0, 0, 0)

def is_valid(state):
    m_left, c_left, _ = state
    m_right = 3 - m_left
    c_right = 3 - c_left

    if not(0 <= m_left <= 3 and 0 <= c_left <= 3):
        return False
    if m_left > 0 and m_left < c_left:
        return False
    if m_right > 0 and m_right < c_right:
        return False
    
    return True

def get_child(state):
    children = []
    m_left, c_left, b = state

    moves = [
        (1, 0),
        (2, 0),
        (0, 1),
        (0, 2),
        (1, 1)
    ]

    for move_m, move_c in moves:
        if b == 1:
            child = (m_left - move_m, c_left - move_c, 0)
        else:
            child = (m_left + move_m, c_left + move_c, 1)
        if is_valid(child):
            children.append(child)
    return children

def h(state):
    ml, cl, _ = state
    return ml+cl

def build_graph(start= START):
    graph = {}
    w_graph = {}
    h_table = {}

    queue = deque([start])
    visited = {start}

    while queue:
        state = queue.popleft()
        children = get_child(state)

        graph[state] = children
        w_graph[state] = [(c, 1) for c in children]
        h_table[state] = h(state)

        for child in children:
            if child not in visited:
                visited.add(child)
                queue.append(child)

    return graph, w_graph, h_table, start, {GOAL}

def print_path(path, total_cost = None):
    if path is None:
        print("Khong tim thay duong di")
        return 
    if total_cost is None:
        total_cost = len(path) -1

    print("Duong di: ")
    for step, item in enumerate(path):
        if isinstance(item, tuple) and len(item) == 2 and isinstance(item[0], tuple):
            state, action = item
            print(f'Step {step}: state= {state}, action= {action}')
        else:
            print(f"Step {step}: {item}")
    print(f"Tong chi phi= {total_cost}")


class BFS:
    def __init__(self, graph:dict, start, goal):
        self.start = start
        self.graph = graph
        self.goal = set(goal) if not isinstance(goal, set) else goal

    def bfs(self, verbose:bool= False):
        op = deque([self.start])
        closed = []
        parent = {self.start:None}
        step = 0

        while op:
            x = op.popleft()
            step+=1

            if verbose:
                print(f'Step {step}: x= {x}, open= {op}, closed= {closed}')
            
            if x in self.goal:
                closed.append(x)
                return self._reconstruct(parent, x), closed
            
            closed.append(x)

            for child in self.graph.get(x, []):
                if child not in op and child not in closed:
                    op.append(child)
                    parent[child] = x
        return None, closed
    
    def _reconstruct(self, parent, goal):
        path, cur = [], goal
        while cur is not None:
            path.append(cur)
            cur = parent[cur]
        return list(reversed(path))
    
graph, _, h_table, start, goal = build_graph()
search = BFS(graph= graph, start=start, goal=goal)
path,_ = search.bfs()
print_path(path=path, total_cost=None)


