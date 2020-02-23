"""We have four rods and a number of disks of different sizes which can slide onto any rod.
The puzzle starts with the disks in a neat stack in ascending order of size on a single rod,
the smallest at the top, thus making a conical shape. The objective of the puzzle is to move
the entire stack to another rod, obeying the following simple rules:
* Only one disk can be moved at a time.
* Each move consists of taking the upper disk from one of the stacks and placing it on top
  of another stack i.e. a disk can only be moved if it is the uppermost disk on a stack.
* No disk may be placed on top of a smaller disk."""

from search import Problem, breadth_first_graph_search
from collections import namedtuple
State=namedtuple("S", ["disk","rod"])

class Hanoi(Problem):
    """the traditional game"""
    def __init__(self, size):
        self.size = size
        super().__init__("1" * size, "2" * size)

    def actions(self, state):
        """Three rods -> 6 actions"""
        acts = []
        f1 = state.find("1")
        f2 = state.find("2")
        f3 = state.find("3")
        f4 = state.find("4")
        if -1 < f1 and (f1 < f2 or f2 == -1):
            acts.append(State(f1, "2"))
        if -1 < f1 and (f1 < f3 or f3 == -1):
            acts.append(State(f1, "3"))
        if -1 < f1 and (f1 < f4 or f4 == -1):
            acts.append(State(f1, "4"))

        if -1 < f2 and (f2 < f1 or f1 == -1):
            acts.append(State(f2, "1"))
        if -1 < f2 and (f2 < f3 or f3 == -1):
            acts.append(State(f2, "3"))
        if -1 < f2 and (f2 < f4 or f4 == -1):
            acts.append(State(f2, "4"))

        if -1 < f3 and (f3 < f1 or f1 == -1):
            acts.append(State(f3, "1"))
        if -1 < f3 and (f3 < f2 or f2 == -1):
            acts.append(State(f3, "2"))
        if -1 < f3 and (f3 < f4 or f4 == -1):
            acts.append(State(f3, "4"))

        if -1 < f4 and (f4 < f1 or f1 == -1):
            acts.append(State(f4, "1"))
        if -1 < f4 and (f4 < f2 or f2 == -1):
            acts.append(State(f4, "2"))
        if -1 < f4 and (f4 < f3 or f3 == -1):
            acts.append(State(f4, "3"))
        return acts

    def result(self, state, action):
        """we change the number denoting rod"""
        disk, char = action
        return state[0:disk] + char + state[disk+1:]

    def value(self, state):
        """we have no good heuristics"""
        return self.size-state.count("2")

if __name__ == "__main__":
    hanoi = Hanoi(4)
    print(breadth_first_graph_search(hanoi).solution())
