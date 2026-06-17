class IterativeDeepeningSearch:
    def __init__(self, graph: dict, start, goals):
        self.graph = graph
        self.start = start
        self.goals = {goals} if isinstance(goals, str) else set(goals)

    def ids(self, max_depth: int, verbose: bool = False):
        all_closed = []

        for depth in range(max_depth + 1):
            closed = []
            parent = {self.start: None}
            step = [0]

            if verbose:
                print(f"Gioi han do sau = {depth}:")

            found = self._dls(
                self.start, depth, closed, parent, step, verbose
            )
            all_closed.extend(closed)

            if found is not None:
                return self._reconstruct(parent, found), all_closed

            if verbose:
                print(f"Khong tim thay o do sau {depth}\n")

        return None, all_closed

    def _dls(self, node, depth_limit, closed, parent, step, verbose=False):
        step[0] += 1
        closed.append(node)

        if node in self.goals:
            if verbose:
                print(
                    f"Buoc {step[0]}:\n"
                    f"X = {node}, depth = {depth_limit},\n"
                    f"open = [],\n"
                    f"close = {closed}\n"
                )
            return node

        if depth_limit == 0:
            if verbose:
                print(
                    f"Buoc {step[0]}:\n"
                    f"X = {node}, depth = {depth_limit},\n"
                    f"open = [],\n"
                    f"close = {closed}\n"
                )
            return None

        children = [
            child for child in self.graph.get(node, [])
            if child not in closed
        ]

        if verbose:
            print(
                f"Buoc {step[0]}:\n"
                f"X = {node}, depth = {depth_limit},\n"
                f"open = {children},\n"
                f"close = {closed}\n"
            )

        for child in children:
            parent[child] = node
            found = self._dls(
                child, depth_limit - 1, closed, parent, step, verbose
            )
            if found is not None:
                return found

        return None

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
