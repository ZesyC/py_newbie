from collections import deque

class BFS:
    def __init__(self, graph:dict, start, goal):
        self.graph = graph
        self.start = start
        self.goal = set(goal) if not isinstance(goal, set) else goal

    def bfs(self, verbose: bool = False):
        op = deque([self.start])
        closed = []
        parent = {self.start:None}

        step = 0
        while op:
            x = op.popleft()
            step+=1

            if verbose:
                print(f'Step {step}: x = {x}, open = {op}, closed = {closed}')

            if x in self.goal:
                closed.append(x)
                return self._reconstruct(parent, x), closed
            
            closed.append(x)

            for child in self.graph.get(x, []):
                if child not in op and child not in closed:
                    op.append(child)
                    parent[child] = x

        return None, closed
    
    def _reconstruct(self, parent, goal):
        path, cur = [], goal
        while cur is not None:
            path.append(cur)
            cur = parent[cur]
        return list(reversed(path))
    
    