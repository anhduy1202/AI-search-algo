#!/usr/bin/python3
from uniform_search import *
from informed_search import *

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
        "Bob": ["Mary", "Jane", "Ivan"],
        "Mary": ["Goldman", "Beth", "Sullivan"],
        "Jane": ["Kiev"],
        "Ivan": [],
        "Goldman": [],
        "Beth": [],
        "Sullivan": [],
        "Kiev": ["Gale"],
        "Gale": [],
    }
    dfs = DepthFirstTreeSearch(graph, "E", "B")
    # dfs.with_loop_checking()
    # bfs = BreadthFirstSearch(graph, "E", "B")
    # ids  = IterativeDeepening(graph2, "Bob", "Gale")
    # print(ids.solve(max_depth=3))

    ### Uniform Search
    weighted_graph = {
        "A": [("S", 1), ("L", 4)],
        "B": [("S", 1), ("D", 2), ("F", 1), ("E", 2)],
        "C": [("S", 2), ("E", 1)],
        "D": [("J", 2), ("H", 1), ("B", 2)],
        "E": [("B", 2), ("C", 1), ("M", 2)],
        "F": [("B", 1), ("P", 2), ("H", 2)],
        "G": [("P", 2)],
        "H": [("D", 1), ("F", 2)],
        "J": [("D", 2), ("K", 1)],
        "K": [("J", 1)],
        "L": [("A", 4)],
        "M": [("E", 2), ("N", 1)],
        "N": [("M", 1)],
        "P": [("F", 2), ("G", 2)],
        "S": [("A", 1), ("B", 1), ("C", 2)],
    }
    ucs = UniformCostSearch(weighted_graph, ("S", 0), "G")
    ucs.solve()
