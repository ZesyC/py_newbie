class IDA:
    def __init__(self, graph: dict, heuristic:dict, start, goal, alpha = 1):
        self.graph = graph
        self.heuristic = heuristic
        self.goal = {goal} if isinstance else set(goal)
        self.alpha = alpha
        self.start = start

    def _f_score(self, cost_from_start, node):
        return cost_from_start + self.alpha*self.heuristic[node]
    
    def ida(self, verbose:bool = False):
        threshold = self._f_score(0, self.start)
        closed = []
        it = 0

        while True:
            path = [self.start]
            visited = {self.start}
            it = 1

            if verbose:
                print(
                    f"Lần lặp {it}:\n"
                    f'threshold = {threshold}'
                )

            next_threshold, result, total_cost = self._search(
                x = self.start,
                cost_from_start = 0,
                threshold = threshold,
                path = path,
                visited = visited,
                closed = closed,
                verbose = verbose
            )

            if result is not None:
                return result, closed, total_cost
            
            if next_threshold == float('inf'):
                return None, closed, float('inf')
            
            threshold = next_threshold

    def _search(self, x, cost_from_start, threshold, path, visited, closed, verbose):
        current_f = self._f_score(cost_from_start, x)
        closed.append(x)

        if verbose:
            print(
                f"x = {x}, g(x) = {cost_from_start},"
                f"h(x) = {self.heuristic[x]}, f(x) = {current_f}, \n"
                f"path = {path}\n"
            )
        
        if current_f > threshold:
            return current_f, None, float('inf')
        
        if x in self.goal:
            return current_f, path.copy(), cost_from_start
        
        next_threshold = float('inf')

        for child, cost in self.graph.get(x, []):
            if child in visited:
                continue

            path.append(child)
            visited.add(child)

            result_threshold, result, total_cost = self._search(
                x = child, 
                cost_from_start= cost_from_start + cost,
                threshold=threshold,
                path= path, 
                visited=visited,
                closed=closed,
                verbose=verbose
            )

            if result is not None:
                return result_threshold, result, total_cost
            
            next_threshold = min(next_threshold, result_threshold)
            path.pop()
            visited.remove(child)

        return next_threshold, None, float('inf')
    