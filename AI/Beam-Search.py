class Beam_search:
    def __init__(self, graph: dict, heuristic: dict, start, goals, width):
        self.graph = graph
        self.heuristic = heuristic
        self.start = start
        self.goals = set(goals) if not isinstance(goals, set) else goals
        self.width = width

    def beam(self, verbose: bool = False):
        op = [self.start]
        close = []
        parent = {self.start: None}

        step = 0
        while op:
            next_op = []

            for x in op:
                step += 1
                if verbose:
                    print(f"Bước {step}:\nX = {x},\nopen = {op},\nclose = {close}\n")

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
            if verbose:
                print(f"open sau khi chọn {self.width} nút tốt nhất = {op}\n")

        return None, close

    def reconstruct(self, parent, goal):
        path, cur = [], goal
        while cur is not None:
            path.append(cur)
            cur = parent[cur]
        return list(reversed(path))


def bai1():
    graph = {
        'S': ['A', 'D'],
        'A': ['B', 'C'],
        'D': ['E', 'F'],
        'B': [],
        'C': [],
        'E': ['G'],
        'F': ['G'],
        'G': []
    }
    heuristic = {
        'S': 12, 'A': 10, 'D': 9, 'B': 7,
        'C': 8, 'E': 6, 'F': 4, 'G': 0
    }
    edge_cost = {
        ('S', 'A'): 4, ('S', 'D'): 3,
        ('A', 'B'): 5, ('A', 'C'): 2,
        ('D', 'E'): 6, ('D', 'F'): 3,
        ('F', 'G'): 5, ('E', 'G'): 2
    }

    find = Beam_search(graph, heuristic, start='S', goals='G', width=2)
    path, close = find.beam(verbose=True)
    print(f"Thứ tự các nút được xét: {' -> '.join(close)}")
    if path is None:
        print("Không tìm thấy đường đi từ S đến G.")
        return

    total_cost = sum(edge_cost[(a, b)] for a, b in zip(path, path[1:]))
    print(f"Đường đi tìm được: {' -> '.join(path)}")
    print(f"Tổng chi phí đường đi: {total_cost}")


bai1()
