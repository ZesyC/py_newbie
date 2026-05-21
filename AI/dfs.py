class DFSGraphSearch:
    def __init__(self, graph: dict, start, goals):
        self.graph = graph
        self.start = start
        self.goals = set(goals) if not isinstance(goals, set) else goals

    def dfs(self, verbose: bool = False):
        op = [self.start]
        closed = []
        parent = {self.start: None}

        step = 0
        while op:
            x = op.pop()
            step+=1
            if verbose:
                print(f"Bước {step}:\nX = {x},\nopen = {op},\nclose = {closed}\n")

            if x in self.goals:
                closed.append(x)
                return self._reconstruct(parent, x), closed
            
            closed.append(x)

            for child in reversed(self.graph.get(x,[])):
                if child not in closed and child not in op:
                    op.append(child)
                    parent[child] = x

        return None, closed
    
    def _reconstruct(self, parent, goals):
        path, cur, = [], goals
        while cur is not None:
            path.append(cur)
            cur = parent[cur]
        return list(reversed(path))
    
def bai5():
    print('Bài 5: DFS trên đồ thị tổng quát:')
    graph = {
        'A': ['B', 'C', 'D'], 'B': ['E', 'F'], 'C': ['G', 'H'],
         'D': ['I', 'J'], 'E': ['K', 'L', 'M'], 'F': [],
        'G': ['N'], 'H': ['O', 'P'], 'I': ['P', 'Q'],
        'J': ['R'], 'K': ['S'], 'L': ['T'], 'M': [],
        'N': [], 'O': [], 'P': ['U'], 'Q': [], 'R': [],
        'S': [], 'T': [], 'U': [] }

    ds = DFSGraphSearch(graph, start = 'A', goals = {'U'})
    path, closed = ds.dfs(verbose=True)
    if path is not None:
        print(f"Đường đi tìm được: {' - '.join(path)}")
    else:
        print(f'Không tìm thấy đường đi.')
    print(f'Thứ tự duyệt: {closed}')
    print(f'Tổng số nút duyệt: {len(closed)}')

bai5()