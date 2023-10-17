from collections import deque
import heapq


class UniformCostSearch:
    def __init__(self, graph, initial_state, goal_state):
        self.graph = graph
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.frontier = [initial_state]
        self.explored = []
        self.time_complexity = ""
        self.space_complexity = ""
        self.complete = ""
        self.optimal = ""

    def properties(self):
        return f"""
Time complexity: {self.time_complexity}
Space complexity: {self.space_complexity}
Complete: {self.complete}
Optimal: {self.optimal}
Activity: List nodes in increasing path cost
Path cost: length of shortest path from initial node
Pros: Optimal, complete, finds shortest path
Cons: Expensive, space complexity
        """

    def solve(self):
        """
        Initialize frontier with initial state
        Initialize explored to empty
        Loop do
            IF the frontier is empty RETURN FAILURE
            Choose lowest cost node from frontier and remove it
            IF lowest cost node is goal RETURN SUCCESS
            Add node to explored
            FOR every child node of node
                IF child not already on frontier or explored
                    insert child node to frontier
                ELSE IF child is in frontier with higher path cost
                    replace existing frontier node with child node
        """
        self.time_complexity = "O(b^C*/epsilon), C* is cost of optimal solution, epsilon is minimum path cost"
        self.space_complexity = "O(b^C*/epsilon)"
        self.complete = "Yes, assuming best solution has a finite cost and minimum edge cost is positive"
        self.optimal = "Yes"
        print(self.properties())
        while self.frontier:
            self.frontier = sorted(self.frontier, key=lambda x: (x[1], x[0]))
            print(f"Frontier: {self.frontier}")
            node, cost = heapq.heappop(self.frontier)
            if node == self.goal_state:
                print(f"Explored: {self.explored}")
                return True
            self.explored.append(node)
            for child in self.graph[node]:
                if (child[0], cost + child[1]) not in self.frontier and child[
                    0
                ] not in self.explored:
                    heapq.heappush(self.frontier, (child[0], cost + child[1]))
                elif child in self.frontier:
                    # if child has higher path cost, replace it
                    if child[1] > cost + child[1]:
                        self.frontier.remove(child)
                        heapq.heappush(self.frontier, (child[0], cost + child[1]))


class AStarSearch:
    def __init__(self, graph, initial_state, goal_state, heuristic):
        self.graph = graph
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.frontier = [initial_state]
        self.explored = []
        self.time_complexity = ""
        self.space_complexity = ""
        self.complete = ""
        self.optimal = ""
        self.heuristic = heuristic

    def properties(self):
        return f"""
Time complexity: {self.time_complexity}
Space complexity: {self.space_complexity}
Complete: {self.complete}
Optimal: {self.optimal}
"""

    def solve(self):
        """
        Initialize frontier with initial state
        Initialize explored to empty
        Loop do
            IF the frontier is empty RETURN FAILURE
            Choose lowest cost node from frontier and remove it
            IF lowest cost node is goal RETURN SUCCESS
            Add node to explored
            FOR every child node of node
                IF child not already on frontier or explored
                    insert child node to frontier
                ELSE IF child is in frontier with higher path cost
                    replace existing frontier node with child node
        """
        self.time_complexity = "O(b^d), depend on heuristic function"
        self.space_complexity = "O(b^d), b is branching factor, d is depth of optimal solution"
        self.complete = "Terminates even on infinite spaces if a reachable goal exists"
        self.optimal = "Always finds optimal solution if heuristic is admissible"
        print(self.properties())
        while self.frontier:
            self.frontier = sorted(self.frontier, key=lambda x: (x[1], x[0]))
            print(f"Frontier: {self.frontier}")
            node, cost = heapq.heappop(self.frontier)
            if node == self.goal_state:
                print(f"Explored: {self.explored}")
                return True
            self.explored.append(node)
            for child in self.graph[node]:
                new_cost = (cost - self.heuristic[node]) + child[1] + self.heuristic[child[0]]
                if child[0] not in self.frontier and child[0] not in self.explored:
                    heapq.heappush(self.frontier, (child[0], new_cost))
                elif child in self.frontier:
                    # if child has higher path cost, replace it
                    if child[1] > cost + child[1]:
                        self.frontier.remove(child)
                        heapq.heappush(self.frontier, (child[0], new_cost))

