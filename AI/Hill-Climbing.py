class HillClimbingSearch:
    def __init__(self, graph: dict, heuristic: dict, start, goals):
        self.graph = graph
        self.heuristic = heuristic
        self.start = start
        self.goals = {goals} if isinstance(goals, str) else set(goals)

    def hill_climbing(self, verbose: bool = False):
        op = [self.start]
        closed = []
        parent = {self.start: None}

        step = 0
        while op:
            x = op.pop()
            closed.append(x)
            step += 1

            if x in self.goals:
                if verbose:
                    print(
                        f"Buoc {step}:\n"
                        f"X = {x}, h(X) = {self.heuristic[x]},\n"
                        f"open = {op},\n"
                        f"close = {closed}\n"
                    )
                return self._reconstruct(parent, x), closed

            children = [
                child for child in self.graph.get(x, [])
                if child not in closed
            ]

            if not children:
                if verbose:
                    print(
                        f"Buoc {step}:\n"
                        f"X = {x}, h(X) = {self.heuristic[x]},\n"
                        f"open = {op},\n"
                        f"close = {closed}\n"
                    )
                return None, closed

            best_child = min(children, key=lambda node: self.heuristic[node])

            if self.heuristic[best_child] >= self.heuristic[x]:
                if verbose:
                    print(
                        f"Buoc {step}:\n"
                        f"X = {x}, h(X) = {self.heuristic[x]},\n"
                        f"open = {op},\n"
                        f"close = {closed}\n"
                    )
                return None, closed

            op.append(best_child)
            parent[best_child] = x

            if verbose:
                print(
                    f"Buoc {step}:\n"
                    f"X = {x}, h(X) = {self.heuristic[x]},\n"
                    f"open = {op},\n"
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

    print("Bai 1: Hill Climbing tu S den G:")
    search = HillClimbingSearch(graph, heuristic, start='S', goals={'G'})
    path, closed = search.hill_climbing(verbose=True)

    if path is not None:
        total_cost = sum(edge_cost[(a, b)] for a, b in zip(path, path[1:]))
        print(f"Duong di tim duoc: {' - '.join(path)}")
        print(f"Tong chi phi duong di: {total_cost}")
    else:
        print("Khong tim thay duong di.")

    print(f"Thu tu duyet: {closed}")
    print(f"Tong so nut duyet: {len(closed)}")


if __name__ == "__main__":
    bai1()
