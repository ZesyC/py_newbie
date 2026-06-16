class BS:
    def __init__(self, graph:dict, heuristic:dict, goal, start, width):
        self.heuristic = heuristic
        self.start = start
        self.width = width
        self.graph = graph 
        self.goal = {goal} if not isinstance(goal, str) else set(goal)

    def bs(self, verbose:bool = False):
        op = [self.start]
        closed = []
        parent = {self.start:None}

        step = 0

        while op:
            step+=1
            next_op = []

            for x in op:
                x = op.pop()
                
                if x in self.goal:
                    closed.append(x)
                    return self._reconstruct(parent, x), closed
                
                closed.append(x)

                for child in self.graph.get(x, []):
                    next_op.append(child)
                    parent[child] = x
            
            next_op.sort(key=lambda node: self.heuristic[node])
            op = next_op[:self.width]

        return None, closed    
    def _reconstruct(self, parent, goal):
        path, cur = [], goal
        while cur is not None:
            path.append(cur)
            cur = parent[cur]
        return list(reversed(path))
