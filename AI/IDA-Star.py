class IDAStarSearch:
    def __init__(self, graph: dict, heuristic: dict, start, goals, alpha=2):
        self.graph = graph
        self.heuristic = heuristic
        self.start = start
        self.goals = {goals} if isinstance(goals, str) else set(goals)
        self.alpha = alpha

    def ida_star(self, verbose: bool = False):
        threshold = 0

        while True:
            if verbose:
                print(f"\nThreshold = {threshold}:")

            op = [(self._f_score(0, self.start), 0, self.start)]
            closed = []
            parent = {self.start: None}
            next_threshold = float('inf')
            step = 0

            while op:
                op.sort(key=lambda x: x[0], reverse=True)
                f_current, g_current, x = op.pop()
                step += 1

                if x in self.goals:
                    closed.append(x)
                    if verbose:
                        open_nodes = [node[2] for node in op]
                        print(
                            f"Buoc {step}:\n"
                            f"X = {x}, f(X) = {f_current},\n"
                            f"open = {open_nodes},\n"
                            f"close = {closed}\n"
                        )
                    return self._reconstruct(parent, x), closed, g_current

                closed.append(x)

                for child, cost in self.graph.get(x, []):
                    cur = x
                    in_path = False
                    while cur is not None:
                        if cur == child:
                            in_path = True
                            break
                        cur = parent[cur]
                    if in_path:
                        continue

                    g_child = g_current + cost
                    f_child = self._f_score(g_child, child)

                    if f_child <= threshold:
                        op.append((f_child, g_child, child))
                        parent[child] = x
                    else:
                        next_threshold = min(next_threshold, f_child)

                if verbose:
                    open_nodes = [node[2] for node in op]
                    print(
                        f"Buoc {step}:\n"
                        f"X = {x}, f(X) = {f_current},\n"
                        f"open = {open_nodes},\n"
                        f"close = {closed}\n"
                    )

            if next_threshold == float('inf'):
                return None, closed, float('inf')

            threshold += self.alpha

    def _f_score(self, cost_from_start, node):
        return cost_from_start + self.heuristic[node]


    def _reconstruct(self, parent, goal):
        path, cur = [], goal
        while cur is not None:
            path.append(cur)
            cur = parent[cur]
        return list(reversed(path))


def bai2():
    graph = {
        'S': [('A', 1), ('B', 1)],
        'A': [('S', 1), ('B', 9)],
        'B': [('S', 1), ('A', 9), ('C', 6), ('G', 12)],
        'C': [('B', 6), ('G', 5)],
        'G': [('B', 12), ('C', 5)]
    }
    heuristic = {
        'S': 7,
        'A': 10,
        'B': 9,
        'C': 5,
        'G': 0
    }

    alpha = 2
    print(f"Bai 2: IDA* tu S den G voi alpha = {alpha}:")
    search = IDAStarSearch(
        graph, heuristic, start='S', goals={'G'}, alpha=alpha
    )
    path, closed, total_cost = search.ida_star(verbose=True)

    if path is not None:
        print(f"Duong di tim duoc: {' - '.join(path)}")
        print(f"Tong chi phi duong di: {total_cost}")
    else:
        print("Khong tim thay duong di.")

    print(f"Tong so nut duyet: {len(closed)}")


if __name__ == "__main__":
    bai2()
