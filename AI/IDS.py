class IterativeDeepeningSearch:
    def __init__(self, graph: dict, start, goals):
        self.graph = graph
        self.start = start
        self.goals = {goals} if isinstance(goals, str) else set(goals)

    def ids(self, max_depth: int = 50, verbose: bool = False):
        all_closed = []

        for limit in range(max_depth + 1):
            op = [(self.start, [self.start])]
            closed = []
            parent = {self.start: None}
            step = 0

            if verbose:
                print(f"Gioi han do sau = {limit}:")

            while op:
                x, path = op.pop()
                step += 1
                depth = len(path) - 1

                closed.append(x)

                if x in self.goals:
                    all_closed.extend(closed)
                    if verbose:
                        print(
                            f"Buoc {step}:\n"
                            f"X = {x}, depth = {depth},\n"
                            f"open = {[node for node, _ in op]},\n"
                            f"close = {closed}\n"
                        )
                    return self._reconstruct(parent, x), all_closed

                if depth < limit:
                    for child in reversed(self.graph.get(x, [])):
                        if child not in path:
                            op.append((child, path + [child]))
                            parent[child] = x

                if verbose:
                    print(
                        f"Buoc {step}:\n"
                        f"X = {x}, depth = {depth},\n"
                        f"open = {[node for node, _ in op]},\n"
                        f"close = {closed}\n"
                    )

            all_closed.extend(closed)

            if verbose:
                print(f"Khong tim thay o do sau {limit}\n")

        return None, all_closed
    def _reconstruct(self, parent, goal):
        path, cur = [], goal
        while cur is not None:
            path.append(cur)
            cur = parent[cur]
        return list(reversed(path))


def bai7():
    print("Bai 7: IDS tren do thi tong quat:")
    graph = {
        'A': ['B', 'C', 'D'], 'B': ['E', 'F'], 'C': ['G', 'H'],
        'D': ['I', 'J'], 'E': ['K', 'L', 'M'], 'F': [],
        'G': ['N'], 'H': ['O', 'P'], 'I': ['P', 'Q'],
        'J': ['R'], 'K': ['S'], 'L': ['T'], 'M': [],
        'N': [], 'O': [], 'P': ['U'], 'Q': [], 'R': [],
        'S': [], 'T': [], 'U': []
    }

    search = IterativeDeepeningSearch(graph, start='A', goals='U')
    path, closed = search.ids(max_depth=5, verbose=True)

    if path is not None:
        print(f"Duong di tim duoc: {' - '.join(path)}")
    else:
        print("Khong tim thay duong di.")

    print(f"Thu tu duyet: {closed}")
    print(f"Tong so nut duyet: {len(closed)}")


if __name__ == "__main__":
    bai7()
