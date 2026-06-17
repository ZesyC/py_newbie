from collections import deque


class BreadthFirstSearch:
    def __init__(self, graph: dict, start, goals):
        self.graph = graph
        self.start = start
        self.goals = {goals} if isinstance(goals, str) else set(goals)

    def bfs(self, verbose: bool = False):
        op = deque([self.start])
        closed = []
        parent = {self.start: None}

        step = 0
        while op:
            x = op.popleft()
            step += 1

            closed.append(x)

            if x in self.goals:
                if verbose:
                    print(
                        f"Buoc {step}:\n"
                        f"X = {x},\n"
                        f"open = {list(op)},\n"
                        f"close = {closed}\n"
                    )
                return self._reconstruct(parent, x), closed

            for child in self.graph.get(x, []):
                if child not in closed and child not in op:
                    op.append(child)
                    parent[child] = x

            if verbose:
                print(
                    f"Buoc {step}:\n"
                    f"X = {x},\n"
                    f"open = {list(op)},\n"
                    f"close = {closed}\n"
                )

        return None, closed

    def _reconstruct(self, parent, goal):
        path, cur = [], goal
        while cur is not None:
            path.append(cur)
            cur = parent[cur]
        return list(reversed(path))


def bai1():
    print("Bai 1: BFS tren do thi tong quat:")
    graph = {
        'A': ['B', 'C', 'D'], 'B': ['E', 'F'], 'C': ['G', 'H'],
        'D': ['I', 'J'], 'E': ['K', 'L', 'M'], 'F': [],
        'G': ['N'], 'H': ['O', 'P'], 'I': ['P', 'Q'],
        'J': ['R'], 'K': ['S'], 'L': ['T'], 'M': [],
        'N': [], 'O': [], 'P': ['U'], 'Q': [], 'R': [],
        'S': [], 'T': [], 'U': []
    }

    search = BreadthFirstSearch(graph, start='A', goals={'U'})
    path, closed = search.bfs(verbose=True)

    if path is not None:
        print(f"Duong di tim duoc: {' - '.join(path)}")
    else:
        print("Khong tim thay duong di.")

    print(f"Thu tu duyet: {closed}")
    print(f"Tong so nut duyet: {len(closed)}")


if __name__ == "__main__":
    bai1()
