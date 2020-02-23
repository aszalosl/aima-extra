"""We have three rods and a number of disks of different sizes which can slide onto any rod.
Each disk has two distinct sides North and South (typically colored red and blue).
The puzzle starts with the disks in a neat stack in ascending order of size on a single rod,
the smallest on top, thus making a conical shape. The objective of the puzzle is to move the
entire stack to another rod, obeying the following simple rules:
* Only one disk can be moved at a time.
* Each move consists of taking the upper disk from one of the stacks and placing it on top of
  another stack i.e. a disk can only be moved if it is the uppermost disk on a stack.
* No disk may be placed on top of a smaller disk.
* Disks must not be placed together with similar poles — 
  magnets in each disk prevent this illegal move.
* Each disk must be flipped as it is moved."""

from search import Problem, breadth_first_search
from collections import namedtuple
State = namedtuple("State", ["frm", "to"])

class Hanoi(Problem):
    """magnetic towers"""
    def __init__(self, size):
        """put tree towers on the rods"""
        def tower(size, flipped):
            """give an n-tuple of color c"""
            return tuple((i, flipped) for i in range(1, size+1))

        self.initial = (tower(size, True), (), ())
        self.goal = [((), (), tower(size, True)), ((), (), tower(size, False))]  # we give a list

    def actions(self, state):
        r1, r2, r3 = state
        acts = []
        if len(r1) > 0:  # not empty
            if len(r2) == 0 or (r1[0][0] <= r2[0][0] and r1[0][1] != r2[0][1]):  # empty or bigger
                acts.append(State(1, 2))
            if len(r3) == 0 or (r1[0][0] <= r3[0][0] and r1[0][1] != r3[0][1]):
                acts.append(State(1, 3))
        if len(r2) > 0:
            if len(r1) == 0 or (r2[0][0] <= r1[0][0] and r2[0][1] != r1[0][1]):
                acts.append(State(2, 1))
            if len(r3) == 0 or (r2[0][0] <= r3[0][0] and r2[0][1] != r3[0][1]):
                acts.append(State(2, 3))
        if len(r3) > 0:
            if len(r1) == 0 or (r3[0][0] <= r1[0][0] and r3[0][1] != r1[0][1]):
                acts.append(State(3, 1))
            if len(r2) == 0 or (r3[0][0] <= r2[0][0] and r3[0][1] != r2[0][1]):
                acts.append(State(3, 2))
        return acts

    def result(self, state, action):
        source, target = action                           # break action into numbers
        source -= 1                                       # indices start at 0
        target -= 1
        state_list = [list(state[0]), list(state[1]), list(state[2])]
        disk = state_list[source][0]                      # store the first element
        if disk[1]:
            disk = (disk[0], False)
        else:
            disk = (disk[0], True)
        state_list[source] = state_list[source][1:]       # delete it
        state_list[target] = [disk] + state_list[target]  # put back on a different rod
        return (tuple(state_list[0]), tuple(state_list[1]), tuple(state_list[2]))

    def value(self, state):
        """we have no good heuristics"""
        return 0

    def goal_test(self, state):
        """we have a list of states"""
        return state in self.goal


if __name__ == "__main__":
    hanoi = Hanoi(4)
    print(breadth_first_search(hanoi).solution())
