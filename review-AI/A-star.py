class AS:
    def __init__(self, graph:dict, heuristic:dict, start, goal, alpha=1):
        self.start = start
        self.graph = graph
        self.alpha = alpha
        self.heuristic = heuristic
        self.goal = {goal} if not isinstance(goal, str) else set(goal)

    def _f_score(self, cost_from_start, node):
        return cost_from_start + self.alpha*self.heuristic[node]

    def a_start(self, verbose:bool = False):
        op = [self.start]
        closed = []
        parent = {self.start:None}
        g_score = {self.start:0}
        best_goal = None
        best_cost = float('inf')
        step = 0

        while op:
            op.sort(key= lambda node: self._f_score(g_score[node], node))
            x = op.pop()

            step+=1
            if verbose:
                print(f'')

            if x in self.goal:
                closed.append(x)

                if g_score[x] < best_cost:
                    best_cost = g_score[x]
                    best_goal = x

                if not op or min(self._f_score(g_score.get(node, float('inf')),node) for node in op) >= best_cost:
                    return self._reconstruct(parent, best_goal), closed, best_cost
                
            for child, cost in self.graph.get(x, []):
                new_cost = g_score[x] + cost
                old_cost = g_score.get(child, float('inf'))

                if child in closed or new_cost >= old_cost:
                    continue

                if child not in op or old_cost < new_cost:
                    parent[child] = x
                    g_score[child] = new_cost

                    if child not in op:
                        op.append(child)

            if best_goal is not None:
                return self._reconstruct(parent, best_goal), closed, best_cost

        return None, closed, best_cost


    def _reconstruct(self, parent, goal):
        path, cur = [], goal
        while cur is not None:
            path.append(cur)
            cur = parent[cur]
        return list(reversed(path)) 


