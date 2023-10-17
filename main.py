#!/usr/bin/python3
from uniform_search import *

# Main 
if __name__ == "__main__":
    graph = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F", "G"],
        "D": ["E"],
        "E": ["C", "F", "H"],
        "F": [],
        "G": ["A"],
        "H": [],
    }
    graph2 = {
        "Bob": ['Mary', 'Jane', 'Ivan'],
        "Mary": ['Goldman','Beth', 'Sullivan'],
        "Jane": ['Kiev'],
        "Ivan": [],
        "Goldman": [],
        "Beth": [],
        "Sullivan": [],
        "Kiev": ['Gale'],
        "Gale": [],
    }
    dfs = DepthFirstTreeSearch(graph, "E", "B")
    # dfs.with_loop_checking()
    # bfs = BreadthFirstSearch(graph, "E", "B")
    ids  = IterativeDeepening(graph2, "Bob", "Gale")
    print(ids.solve(max_depth=3))