#!/usr/bin/env python3
from uninformed_search import *
from informed_search import *
from adversarial_search import *
from game_tree import *

# Main
if __name__ == "__main__":
    
    """ Uninformed Search """
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
    # graph = {
    #     "A": ["B", "C"],
    #     "B": ["D", "E"],
    #     "C": ["F", "G"],
    #     "D": ["E"],
    #     "E": ["C", "F"],
    #     "F": [],
    #     "G": []
    # }
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
    # dfs = DepthFirstTreeSearch(graph, "E", "B")
    # dfs.with_loop_checking()
    # bfs = BreadthFirstSearch(graph, "E", "B")
    # bfs.solve()
    # ids  = IterativeDeepening(graph2, "Bob", "Gale")
    # print(ids.solve(max_depth=3))

    """ Informed Search """
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
    # weighted_graph = {
    #     "Arad": [("Zerind", 75), ("Timisoara", 118), ("Sibiu", 140)],
    #     "Zerind": [("Aread", 75), ("Oradea", 71)],
    #     "Oradea": [("Zerind", 71), ("Sibiu", 151)],
    #     "Sibiu": [("Arad", 140), ("Oradea", 151), ("Fagaras", 99), ("Rimicu Vilcea", 80)],
    #     "Timisoara": [("Arad", 118), ("Lugoj", 111)],
    #     "Lugoj": [("Timisoara", 111), ("Mehadia", 70)],
    #     "Mehadia": [("Lugoj", 70), ("Dobreta", 75)],
    #     "Dobreta": [("Mehadia", 75), ("Craiova", 120)],
    #     "Craiova": [("Dobreta", 120), ("Pitesti", 138), ("Rimicu Vilcea", 146)],
    #     "Pitesti": [("Bucharest", 101), ("Craiova", 138), ("Rimicu Vilcea", 97)],
    #     "Rimicu Vilcea": [("Sibiu", 80), ("Pitesti", 97), ("Craiova", 97)],
    #     "Fagaras": [("Bucharest", 211), ("Sibiu", 99)],
    #     "Bucharest": [("Fagaras", 211), ("Pitesti", 101), ("Giurgiu", 90)],
    #     "Giurgiu": [("Bucharest", 90)],
    # }
    # ucs = UniformCostSearch(weighted_graph, ("S", 0), "G")
    # ucs.solve()
    # heuristic_table = {
    #     "Arad": 366,
    #     "Zerind": 374,
    #     "Oradea": 380,
    #     "Sibiu": 253,
    #     "Timisoara": 329,
    #     "Lugoj": 244,
    #     "Mehadia": 241,
    #     "Dobreta": 242,
    #     "Craiova": 160,
    #     "Pitesti": 98,
    #     "Rimicu Vilcea": 193,
    #     "Fagaras": 178,
    #     "Bucharest": 0,
    #     "Giurgiu": 77
    # }
    heuristic_table = {
        "A": 5.1,
        "B": 4.1,
        "C": 3.9,
        "D": 4,
        "E": 2.2,
        "F": 3.8,
        "G": 0,
        "H": 3.7,
        "J": 7,
        "K": 6,
        "L": 4,
        "M": 0.5,
        "N": 1.5,
        "P": 1.8,
        "S": 4.5, 
    }

    a_star = AStarSearch(weighted_graph, ("S", heuristic_table["S"]), "G", heuristic_table)
    a_star.solve()
    
    """ Adversarial Search """

    """Game Tree"""
    # print_game_tree(game_tree_graph, "A")

    # MiniMax = MiniMax()
    # MiniMax.best_move(game_tree_graph, "A", 3)

    # AlphaBeta = AlphaBetaPruning()
    # AlphaBeta.best_move(game_tree_graph, "A", 4)


