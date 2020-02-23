"""We start from the number 4, and with each step we can either put
numbers 0 or 4 to the end of the actual number, or if the number is even,
we can divide it by 2."""

from search import Problem, breadth_first_graph_search
class Four(Problem):
    """game four"""

    def __init__(self, n):
        """set up the goal"""
        self.goal = n
        self.initial = 4

    def actions(self, state):
        """we have three or two actions"""
        return ["0", "4", "/"] if state % 2 == 0 else ["0", "4"]

    def result(self, state, action):
        """the results are obvius"""
        if action == "0":
            return state*10  # extend with 0
        elif action == "4":
            return state*10+4  # extend with 1
        else:
            return state // 2  # divide by 2

    def value(self, state):
        """the number of chars is a suitable heuristics"""
        return abs(len(str(state))-len(str(self.goal)))


if __name__ == "__main__":
    negy = Four(160)
    print(breadth_first_graph_search(negy).solution())
