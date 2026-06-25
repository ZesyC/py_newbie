class GBF:
    def __init__(self, start, goal, graph:dict, heuristic:dict):
        self.start = start
        self.graph = graph
        self.heuristic = heuristic
        self.goal = set(goal) if not isinstance(goal, set) else goal

    def gbf(self, verbose:bool = False):
        op = [self.start]
        closed = []
        parent = {self.start:None}

        step = 0

        while op:
            op.sort(key = lambda node: self.heuristic[node])
            x = op.pop()

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