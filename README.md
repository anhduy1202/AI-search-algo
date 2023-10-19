# About
All graph search algorithms to make my life easier

# Available Algo:
- US: Uninformed Search

- IS: Informed Search (Weighted Graph)

- AS: Adversarial Search (Game Theory)

| Type  | Algo | Note  | Usage |
| ------------- | ------------- | ------------- | ------------- | 
| US | ```DepthFirstTreeSearch()```  |  no loop check  |  `dfs = DepthFirstTreeSearch(graph, "E", "B")` <br/><br/> `dfs.without_loop_checking()`  |
| US | `DepthFirstTreeSearch()`  | loop check |  `dfs = DepthFirstTreeSearch(graph, "E", "B")` <br/><br/> `dfs.with_loop_checking()`  |
| US | `DepthFirstTreeSearch()`  | limited_depth_search |  `dfs = DepthFirstTreeSearch(graph, "E", "B")` <br/><br/> `dfs.limited_depth_search(depth=x)`  |
| US | `BreadthFirstSearch()`  | solve() |  `bfs = BreadthFirstSearch(graph, "E", "B")` <br/><br/> `bfs.solve()`  |
| US | `IterativeDeepening()`  | solve() |  `ids  = IterativeDeepening(graph2, "Bob", "Gale")` <br/><br/> `ids.solve(max_depth=?)`  |
| IS | `UniformCostSearch()`  | solve() |  `ucs = UniformCostSearch(weighted_graph, ("S", 0), "G")` <br/><br/> `ucs.solve()`  |
| IS | `AStarSearch()`  | solve() |  `a_star = AStarSearch(weighted_graph, ("S", heuristic_table["S"]), "G", heuristic_table)` <br/><br/> `a_star.solve()`  |
| AS | `MiniMax()`  | best_move(graph, root, depth) |  `MiniMax = MiniMax()` <br/><br/> `MiniMax.best_move(game_tree_graph, "A", 3)`  |
| AS | `AlphaBeta()`  | best_move(graph, root, depth) |  `AlphaBeta = AlphaBetaPruning()` <br/><br/> `AlphaBeta.best_move(game_tree_graph, "A", 4)`  |