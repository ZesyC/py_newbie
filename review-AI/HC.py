class HC:
    def __init__(self, graph:dict, heuristic:dict, goal, start):
        self.graph = graph
        self.heuristic = heuristic
        self.start = start
        self.goal = set(goal) if not isinstance(goal, set) else goal

    def hc(self, verbose:bool = False):
        op = [self.start]
        closed = []
        parent = {self.start:None}
        step = 0

        while op :
            x = op.pop()
            step+=1

            if verbose:
                print(f'Step {step}, x = {x}, op = {op}, closed = {closed}')

            if x in self.goal:
                closed.append(x)
                return self._reconstruct(parent, x), closed
            
            closed.append(x)

            child = [child for child in self.graph.get(x, []) if child not in closed]

            if not child:
                return None, closed
            
            best_child = min(child, key=lambda node: self.heuristic[node])

            if self.heuristic[best_child] >= self.heuristic[x]:
                return None, closed
            
            op.append(best_child)
            parent[best_child] = x


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

    print("Bài 1: Hill Climbing từ S đến G:")
    search = HC(graph, heuristic, start='S', goal={'G'})
    path, closed = search.hc(verbose=True)

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
