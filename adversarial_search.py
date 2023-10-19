
class MiniMax:
    def __init__(self) -> None:
        pass
    
    def minimax(self, graph, node, depth, maximizing_player):
        if depth == 0 or not graph[node]['children']:
            return graph[node]['value']

        if maximizing_player:
            max_eval = float("-inf")
            for child in graph[node]['children']:
                evaluation = self.minimax(graph, child, depth - 1, False)
                max_eval = max(max_eval, evaluation)
            return max_eval
        else:
            min_eval = float("inf")
            for child in graph[node]['children']:
                evaluation = self.minimax(graph, child, depth - 1, True)
                min_eval = min(min_eval, evaluation)
            return min_eval

    def best_move(self, graph, root, depth):
        best_value = float("-inf")
        best_move = None
        for child in graph[root]['children']:
            value = self.minimax(graph, child, depth - 1, False)
            if value > best_value:
                best_value = value
                best_move = child
        print("Best move:", best_move)
        print("Best value:", best_value)
        return best_move

class AlphaBetaPruning:
    def __init__(self) -> None:
        self.prune_count = 0

    def alpha_beta(self, graph, node, depth, alpha, beta, maximizing_player):
        # Return value for terminal node
        if depth == 0 or not graph[node]['children']:
            return graph[node]['value']
        """
        def max-value(state, a, β):
            initialize v = -∞
            for each successor of state:
                v = max(v, value(successor, a, β))
                if v ≥ β return v
                a = max(a, v)
            return v
        """
        if maximizing_player:
            max_eval = float("-inf")
            for child in graph[node]['children']:
                evaluation = self.alpha_beta(graph, child, depth - 1, alpha, beta, False)
                max_eval = max(max_eval, evaluation)
                if beta <= alpha:
                    print(f"Pruned Node {child} at Node: {node} (Max)\n")
                    self.prune_count += 1
                    continue
                alpha = max(alpha, max_eval)
            print(f"Node {node}: Alpha = {alpha}, Beta = {beta}, Value = {max_eval}")
            return max_eval
        else:
            """
            def min-value(state , a, β):
                initialize v = +∞
                for each successor of state:
                    v = min(v, value(successor, a, β))
                    if v ≤ a return v
                    β = min(β, v)
                return v
            """
            min_eval = float("inf")
            for child in graph[node]['children']:
                evaluation = self.alpha_beta(graph, child, depth - 1, alpha, beta, True)
                min_eval = min(min_eval, evaluation)
                if beta <= alpha:
                    print(f"Pruned Node {child} at Node {node} (Min)\n")
                    self.prune_count += 1
                    continue
                beta = min(beta, min_eval)
            print(f"Node {node}: Alpha = {alpha}, Beta = {beta}, Value = {min_eval}")
            return min_eval

    def best_move(self, graph, root, depth):
        best_value = float("-inf")
        best_move = None
        alpha = float("-inf")
        beta = float("inf")
        for child in graph[root]['children']:
            value = self.alpha_beta(graph, child, depth - 1, alpha, beta, False)
            if value > best_value:
                best_value = value
                best_move = child
            alpha = max(alpha, best_value)
        print("====================================")
        print("\nBest move:", best_move)
        print("Best value:", best_value)
        print("Prune count:", self.prune_count)
        return best_move


def print_game_tree(graph, node, depth=0):
    if node is None:
        return
    print("  " * depth + f"({node}, {graph[node]['value']})")
    for child in graph[node]['children']:
        print_game_tree(graph, child, depth + 1)