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

            if verbose:
                print(
                    f"Bước {step}:\n"
                    f"X = {x},\n"
                    f"open = {list(op)},\n"
                    f"close = {closed}\n"
                )

            if x in self.goals:
                closed.append(x)
                return self._reconstruct(parent, x), closed

            closed.append(x)

            for child in self.graph.get(x, []):
                if child not in closed and child not in op:
                    op.append(child)
                    parent[child] = x

        return None, closed

    def _reconstruct(self, parent, goal):
        path, cur = [], goal
        while cur is not None:
            path.append(cur)
            cur = parent[cur]
        return list(reversed(path))


def bai1():
    print("Bài 1: BFS trên đồ thị tổng quát:")
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
        print(f"Đường đi tìm được: {' - '.join(path)}")
    else:
        print("Không tìm thấy đường đi.")

    print(f"Thứ tự duyệt: {closed}")
    print(f"Tổng số nút duyệt: {len(closed)}")


if __name__ == "__main__":
    bai1()
