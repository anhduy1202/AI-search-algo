from collections import deque


class DepthFirstTreeSearch:
    def __init__(self, graph, initial_state, goal_state):
        self.graph = graph
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.frontier = [initial_state]
        self.explored = []
        self.path = []
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
        """

    def without_loop_checking(self):
        """
        Initialize frontier with initial state
        Loop do
            IF the frontier is empty RETURN FAILURE
            Choose top node and remove it from frontier
            IF top node is goal RETURN SUCCESS
            expand top node: pushing child nodes to the frontier
        """
        self.time_complexity = "O(b^m)"
        self.space_complexity = "O(bm)"
        self.complete = "No (can have loops)"
        self.optimal = "No, It finds the leftmost solution, regardless of depth or cost"
        print(self.properties())
        while True:
            # Time out after 10 iterations
            if len(self.explored) > 10:
                return False
            if not self.frontier:
                return False
            print(f"Frontier: {self.frontier}")
            node = self.frontier.pop()
            if node == self.goal_state:
                print(f"Explored: {self.explored}")
                return True
            self.explored.append(node)
            self.frontier.extend(self.graph[node])

    def with_loop_checking(self):
        """
        frontier: stack
        path: from root to current node
        Initialize frontier with initial state
            Loop do
            IF the frontier is empty RETURN FAILURE
            Choose top node and remove it from frontier
            IF top node is goal RETURN SUCCESSß
            expand top node
            push resulting nodes to the frontier IF they are not
            already on the path
        """
        self.time_complexity = "O(b^m)"
        self.space_complexity = "O(bm)"
        self.complete = "Yes (finite space), No (inf space)"
        self.optimal = "No, It finds the leftmost solution, regardless of depth or cost"
        print(self.properties())
        while True:
            if not self.frontier:
                return False
            print(f"Frontier: {self.frontier}")
            node = self.frontier.pop()
            if node == self.goal_state:
                print(f"Path: {self.path} \n")
                return True
            self.path.insert(0, node)
            print(f"Path: {self.path} \n")
            # Check top node of path lead to dead an, remove it from path
            if self.graph[self.path[0]] == []:
                self.path.pop(0)
            self.frontier.extend(self.graph[node])
            self.frontier = [node for node in self.frontier if node not in self.path]

    def limited_depth_search(self, depth):
        self.time_complexity = "O(b^l)"
        self.space_complexity = "O(bl)"
        self.complete = "Yes"
        self.optimal = "No, It finds the leftmost solution, regardless of depth or cost"
        print(self.properties())
        while True:
            if not self.frontier:
                return False
            print(f"Frontier: {self.frontier}")
            node = self.frontier.pop()
            if node == self.goal_state:
                print(f"Path: {self.path}")
                return True
            self.path.insert(0, node)
            # Check top node of path lead to dead an, remove it from path
            if self.graph[self.path[0]] == []:
                self.path.pop(0)
            else:
                self.path.append(node)
            self.frontier.extend(self.graph[node])
            self.frontier = [node for node in self.frontier if node not in self.path]


class BreadthFirstSearch:
    def __init__(self, graph, initial_state, goal_state):
        self.graph = graph
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.frontier = deque([initial_state])
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
        """

    def solve(self):
        """
        Initialize frontier with initial state
        Initialize explored to empty
        Loop do
            IF the frontier is empty RETURN FAILURE
            Choose front-node from frontier and remove it
            Add front-node to explored
            FOR every child-node of front-node
                IF child-node not already on frontier or explored
                    IF child-node is goal RETURN SUCCESS
                    Add child-node to frontier
        """
        self.time_complexity = "O(b^s), s is depth of shallowest solution"
        self.space_complexity = "O(b^s)"
        self.complete = "Yes"
        self.optimal = "Yes, if all costs are equal"
        print(self.properties())
        while self.frontier:
            print(f"Frontier: {self.frontier}")
            node = self.frontier.popleft()
            if node == self.goal_state:
                print(f"Explored: {self.explored}")
                return True
            print(f"Explored: {self.explored} \n")
            self.explored.append(node)
            for child in self.graph[node]:
                if child not in self.frontier and child not in self.explored:
                    self.frontier.append(child)


class IterativeDeepening:
    def __init__(self, graph, initial_state, goal_state):
        self.graph = graph
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.frontier = []
        self.explored = []
        self.time_complexity = ""
        self.space_complexity = ""
        self.complete = ""
        self.path = []
        self.optimal = ""

    def properties(self):
        return f"""
Time complexity: {self.time_complexity}
Space complexity: {self.space_complexity}
Complete: {self.complete}
Optimal: {self.optimal}
Note: In general, iterative deepening is the preferred uninformed search method when the search space is large and the depth of the solution is not known
        """

    def dfs(self, root, max_depth):
        self.frontier = [(root, 0)]
        while True:
            # Check if frontier is empty
            if not self.frontier:
                return False
            # Remove from frontier if max depth reached
            if self.frontier[-1][1] > max_depth:
                self.frontier.pop()
                continue
            print(f"Frontier: {self.frontier}")
            node, curr_depth = self.frontier.pop()
            if node == self.goal_state:
                return True
            for node in self.graph[node]:
                self.frontier.append((node, curr_depth + 1))

    def solve(self, max_depth):
        self.time_complexity = "O(b^d), d is depth"
        self.space_complexity = "O(bm)"
        self.complete = "Yes"
        self.optimal = "Yes, if all costs are equal"
        print(self.properties())
        return self.dfs(self.initial_state, max_depth)
