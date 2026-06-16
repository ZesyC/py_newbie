class BeamSearch:
    def __init__(self, graph: dict, heuristic: dict, start, goals, width):
        self.graph = graph
        self.heuristic = heuristic
        self.start = start
        self.goals = {goals} if isinstance(goals, str) else set(goals)
        self.width = width

    def beam_search(self, verbose: bool = False):
        op = [self.start]
        closed = []
        parent = {self.start: None}

        step = 0
        while op:
            step += 1
            next_op = []

            if verbose:
                print(
                    f"Bước {step}:\n"
                    f"open = {op},\n"
                    f"close = {closed}\n"
                )

            for x in op:
                if x in self.goals:
                    closed.append(x)
                    return self._reconstruct(parent, x), closed

                closed.append(x)

                for child in self.graph.get(x, []):
                    if child not in closed and child not in next_op:
                        next_op.append(child)
                        parent[child] = x

            next_op.sort(key=lambda node: self.heuristic[node])
            op = next_op[:self.width]

        return None, closed

    def _reconstruct(self, parent, goal):
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

    width = 2
    print(f"Bài 1: Beam Search từ S đến G với width = {width}:")
    search = BeamSearch(
        graph, heuristic, start='S', goals={'G'}, width=width
    )
    path, closed = search.beam_search(verbose=True)

    if path is not None:
        total_cost = sum(edge_cost[(a, b)] for a, b in zip(path, path[1:]))
        print(f"Đường đi tìm được: {' - '.join(path)}")
        print(f"Tổng chi phí đường đi: {total_cost}")
    else:
        print("Không tìm thấy đường đi.")

    print(f"Thứ tự duyệt: {closed}")
    print(f"Tổng số nút duyệt: {len(closed)}")


if __name__ == "__main__":
    bai1()
