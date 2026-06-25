class IDA:
    def __init__(self, graph: dict, heuristic:dict, start, goal, alpha = 2):
        self.graph = graph
        self.heuristic = heuristic
        self.goal = {goal} if isinstance else set(goal)
        self.alpha = alpha
        self.start = start

    def _f_score(self, cost_from_start, node):
        return cost_from_start + self.heuristic[node]
    
    def ids_star(self, verbose:bool = False):
        threshold = 0

        while True:
            op= [(self._f_score(0, self.start,), 0, self.start)]
            closed = []
            parent = {self.start:None}
            next_threshold = float('inf')
            step = 0

            while op:
                op.sort(key= lambda x: x[0], reverse=True)
                f_cur, g_cur, x = op.pop()
                step+=1

                if x in self.goal:
                    open = [node[2] for node in op]
                    if verbose:
                        print(
                            f'Step {step}:'
                            f'x= {x}, f(x)= {f_cur}'
                            f'open= {open}'
                            f'closed= {closed}'
                        )
                    return self._reconstruct(parent, x), closed, g_cur
                
                closed.append(x)

                for child, cost in self.graph.get(x, []):
                    cur = x
                    in_path = False
                    while cur is not None:
                        if cur == child:
                            in_path = True
                            break
                        if in_path:
                            continue

                    g_child = g_cur + cost
                    f_child = self._f_score(g_child, child)

                    if f_child <= threshold:
                        op.append((f_child, g_child, child))
                        parent[child] = x
                    else:
                        next_threshold = min(next_threshold, f_child)

                if verbose:
                    open = [node[2] for node in op]
                    print(
                        f'Step {step}:'
                        f'x= {x}, f(x)= {f_cur}'
                        f'open= {open}'
                        f'closed= {closed}'
                    )

                if next_threshold == float('inf'):
                    return None, closed, float('inf')
                
                threshold += self.alpha


    
    def _reconstruct(self, parent, goal):
        path, cur = [], goal
        while cur is not None:
            path.append(cur)
            cur = parent[cur]
        return list(reversed(path))