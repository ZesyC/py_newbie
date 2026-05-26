class Beam_search:
    def __init__(self, graph: dict, heuristic: dict, start, goals, width):
        self.graph = graph
        self.heuristic = heuristic
        self.start = start
        self.goals = set(goals) if not isinstance(goals, set) else goals
        self.width = width

    def beam(self):
        op = [self.start]
        close = []
        parent = {self.start: None}

        while op:
            next_op = []

            for x in op:
                if x in self.goals:
                    close.append(x)
                    return self.reconstruct(parent, x), close

                close.append(x)
                for child in self.graph.get(x, []):
                    if child not in close and child not in next_op:
                        next_op.append(child)
                        parent[child] = x

            next_op.sort(key=lambda node: self.heuristic[node])
            op = next_op[:self.width]

        return None, close

    def reconstruct(self, parent, goal):
        path, cur = [], goal
        while cur is not None:
            path.append(cur)
            cur = parent[cur]
        return list(reversed(path))


def bai_1():
    graph = {
        'A': ['B', 'C', 'D'], 'B': ['E', 'F'], 'C': ['G', 'H'],
        'D': ['I', 'J'], 'E': ['K', 'L', 'M'], 'F': [],
        'G': ['N'], 'H': ['O', 'P'], 'I': ['P', 'Q'],
        'J': ['R'], 'K': ['S'], 'L': ['T'], 'M': [],
        'N': [], 'O': [], 'P': ['U'], 'Q': [], 'R': [],
        'S': [], 'T': [], 'U': []
    }
    heuristic = {
        'A': 5, 'B': 6, 'C': 3, 'D': 7, 'E': 8, 'F': 9,
        'G': 5, 'H': 2, 'I': 4, 'J': 8, 'K': 9, 'L': 9,
        'M': 9, 'N': 7, 'O': 6, 'P': 1, 'Q': 6, 'R': 9,
        'S': 8, 'T': 8, 'U': 0
    }

    find = Beam_search(graph, heuristic, start='A', goals='U', width=2)
    path, close = find.beam()
    print(f"Đường đi tìm được: {'-'.join(path) if path else 'Không tìm thấy'}")
    print(f"Tổng số nút đã duyệt: {len(close)}")


bai_1()
