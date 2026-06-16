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

            if verbose:
                print(f"Giới hạn độ sâu = {depth}")

            found = self._dls(self.start, depth, closed, parent, verbose)
            all_closed.extend(closed)

            if found is not None:
                return self._reconstruct(parent, found), all_closed

            if verbose:
                print(f"Không tìm thấy ở độ sâu {depth}\n")

        return None, all_closed

    def _dls(self, node, depth_limit, closed, parent, verbose: bool = False):
        closed.append(node)

        if verbose:
            print(f"X = {node}, độ sâu còn lại = {depth_limit}, close = {closed}")

        if node in self.goals:
            return node

        if depth_limit == 0:
            return None

        for child in self.graph.get(node, []):
            if child not in closed:
                parent[child] = node
                found = self._dls(child, depth_limit - 1, closed, parent, verbose)
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
    print('Bài 7: IDS trên đồ thị tổng quát:')
    graph = {
        'A': ['B', 'C', 'D'], 'B': ['E', 'F'], 'C': ['G', 'H'],
        'D': ['I', 'J'], 'E': ['K', 'L', 'M'], 'F': [],
        'G': ['N'], 'H': ['O', 'P'], 'I': ['P', 'Q'],
        'J': ['R'], 'K': ['S'], 'L': ['T'], 'M': [],
        'N': [], 'O': [], 'P': ['U'], 'Q': [], 'R': [],
        'S': [], 'T': [], 'U': []
    }

    find = IterativeDeepeningSearch(graph, start='A', goals='U')
    path, closed = find.ids(max_depth=5, verbose=True)

    if path is not None:
        print(f"Đường đi tìm được: {' - '.join(path)}")
    else:
        print('Không tìm thấy đường đi.')
    print(f'Thứ tự duyệt: {closed}')
    print(f'Tổng số nút duyệt: {len(closed)}')


bai7()
