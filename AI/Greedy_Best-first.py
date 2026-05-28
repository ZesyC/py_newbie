class Greedy_best_first_search:
    def __init__(self, graph: dict, heuristic: dict, start, goals):
        self.graph = graph
        self.heuristic = heuristic
        self.start = start
        self.goals = {goals} if isinstance(goals, str) else set(goals)

    def greedy(self, verbose: bool = False):
        op = [self.start]
        close = []
        parent = {self.start: None}

        step = 0
        while op:
            op.sort(key=lambda node: self.heuristic[node])
            x = op.pop(0)
            step += 1
            if verbose:
                print(f"Bước {step}:")
                print(f"  Chọn X: {x}(h={self.heuristic[x]})")
                print(f"  open sau khi lấy X: {self.format_nodes(op)}")
                print(f"  close hiện tại: {close}")

            if x in self.goals:
                close.append(x)
                if verbose:
                    print(f"  Gặp đích: {x}\n")
                return self.reconstruct(parent, x), close

            close.append(x)
            children = []
            for child in self.graph.get(x, []):
                if child not in close and child not in op:
                    op.append(child)
                    children.append(child)
                    parent[child] = x
            op.sort(key=lambda node: self.heuristic[node])
            if verbose:
                print(f"  Node con mới thêm: {self.format_nodes(children)}")
                print(f"  open sau khi sắp xếp: {self.format_nodes(op)}\n")

        return None, close

    def reconstruct(self, parent, goal):
        path, cur = [], goal
        while cur is not None:
            path.append(cur)
            cur = parent[cur]
        return list(reversed(path))

    def format_nodes(self, nodes):
        return '[' + ', '.join(
            f"{node}(h={self.heuristic[node]})" for node in nodes
        ) + ']'

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

    print(f"Từ S đến G: ")
    find = Greedy_best_first_search(graph, heuristic, start='S', goals='G')
    path, close = find.greedy(verbose=True)
    print(f"Thứ tự các nút được xét: {' -> '.join(close)}")
    if path is None:
        print("Không tìm thấy đường đi từ S đến G.")
        return

    total_cost = sum(edge_cost[(a, b)] for a, b in zip(path, path[1:]))
    print(f"Đường đi tìm được: {' -> '.join(path)}")
    print(f"Tổng chi phí đường đi: {total_cost}")

    print(f"Từ A đến G: ")
    find2 = Greedy_best_first_search(graph, heuristic, start='A', goals='G')
    path, close = find2.greedy(verbose=True)
    print(f"Thứ tự các nút được xét: {' -> '.join(close)}")
    if path is None:
        print("Không tìm thấy đường đi từ S đến G.")
        return

    total_cost = sum(edge_cost[(a, b)] for a, b in zip(path, path[1:]))
    print(f"Đường đi tìm được: {' -> '.join(path)}")
    print(f"Tổng chi phí đường đi: {total_cost}")


if __name__ == "__main__":
    bai1()
