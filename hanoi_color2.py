"""We have three rods and a number of disks of different sizes which can slide onto any rod.
For every size there are two disks: one black and one white.
The puzzle starts with the disks in a neat stack in ascending order of
size on the first rod in alternating colour, the smallest at the top,
thus making a conical shape. The objective of the puzzle is to make
two monochrome towers on the first two rods obeying the following simple rules:
* Only one disk can be moved at a time.
* Each move consists of taking the upper disk from one of the stacks and
  placing it on top of another stack i.e.
  a disk can only be moved if it is the uppermost disk on a stack.
* No disk may be placed on top of a smaller disk.
"""

from search import Problem, breadth_first_graph_search
from collections import namedtuple
State = namedtuple("State", ["frm", "to"])

class Hanoi(Problem):
    """break bi-color tower into monochrome ones"""
    def __init__(self, size):
        """put tree towers on the rods"""
        def tower(size, color):
            """give an n-tuple of color c"""
            return tuple((i, color) for i in range(1, size+1))

        self.initial = (tuple((i//2, "b" if i % 2 == 0 else "w") \
            for i in range(2, 2*size+2)), (), ())
        self.goal = (tower(size, "b"), tower(size, "w"), ())

    def actions(self, state):
        r1, r2, r3 = state
        acts = []
        if len(r1) > 0:  # not empty
            if len(r2) == 0 or r1[0][0] <= r2[0][0]:  # empty or bigger
                acts.append(State(1, 2))
            if len(r3) == 0 or r1[0][0] <= r3[0][0]:
                acts.append(State(1, 3))
        if len(r2) > 0:
            if len(r1) == 0 or r2[0][0] <= r1[0][0]:
                acts.append(State(2, 1))
            if len(r3) == 0 or r2[0][0] <= r3[0][0]:
                acts.append(State(2, 3))
        if len(r3) > 0:
            if len(r1) == 0 or r3[0][0] <= r1[0][0]:
                acts.append(State(3, 1))
            if len(r2) == 0 or r3[0][0] <= r2[0][0]:
                acts.append(State(3, 2))
        return acts

    def result(self, state, action):
        source, target = action                           # break action into numbers
        source -= 1                                       # indices start at 0
        target -= 1
        state_list = [list(state[0]), list(state[1]), list(state[2])]
        disk = state_list[source][0]                      # store the first element
        state_list[source] = state_list[source][1:]       # delete it
        state_list[target] = [disk] + state_list[target]  # put back on a different rod
        return (tuple(state_list[0]), tuple(state_list[1]), tuple(state_list[2]))

    def value(self, state):
        """we have no good heuristics"""
        return 0

if __name__ == "__main__":
    hanoi = Hanoi(3)
    print(breadth_first_graph_search(hanoi).solution())
