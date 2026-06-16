class DFS:
    def __init__(self, graph:dict, start, goal):
        self.graph = graph
        self.start = start
        self.goal = set(goal) if not isinstance (goal, set) else goal

    def dfs(self, verbose:bool=False):
        op = [self.start]
        closed = []
        parent = {self.start:None}

        step = 0
        while op:
            x = op.pop()
            step+=1

            if verbose:
                print(f"Step: {step}, x = {x}, op = {op}, closed = {closed}")

            if x in self.goal:
                closed.append(x)
                return self._reconstruct(parent, x), closed
            
            closed.append(x)

            for child in reversed(self.graph.get(x, [])):
                if child not in op and child not in closed:
                    op.append(child)
                    parent[child] = x
            
        return None, closed
    
    def _reconstruct(self, parent, goal):
        path, cur = [], goal
        while cur:
            path.append(cur)
            cur = parent[cur]
        return list(reversed(path))
    
    