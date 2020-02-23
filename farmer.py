#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A farmer wants to cross a river and take with him a wolf,
a goat, and a cabbage. There is a boat that can only fit two,
himself plus either the wolf, the goat, or the cabbage.
If the wolf and the goat are alone on one shore,
the wolf will eat the goat. If the goat and the cabbage are
alone on the shore, the goat will eat the cabbage.
"""

from search import Problem, breadth_first_search
#from collections import namedtuple
#State = namedtuple("State", ["farmer/boat", "wolf", "goat", "cabbage"])
class Farmer(Problem):
    "farmer, wolf, goat, cabbage problem"
    def __init__(self):
        """We use logical variables to show one item
        have crossed the river, or not.
        The farmes and the boat moves together,
        hence no need extra storage"""
        self.initial = (False, False, False, False)
        self.goal = (True, True, True, True)

    def actions(self, state):
        farmer, wolf, goat, cabbage = state
        acts = []
        if farmer == wolf and (goat != cabbage):
            # if doesn't left goat and cabbage together
            # can take the wolf
            acts.append("w")
        if farmer == cabbage and (wolf != goat):
            # if doesn't left goat and wolf together
            # can take the cabbage
            acts.append("c")
        if farmer == goat:
            acts.append("g")
        if (wolf != goat) and (goat != cabbage):
            acts.append("-")
        return acts

    def result(self, state, action):
        farmer, wolf, goat, cabbage = state
        if action == "w":
            return (not farmer, not wolf, goat, cabbage)
        if action == "c":
            return (not farmer, wolf, goat, not cabbage)
        if action == "g":
            return (not farmer, wolf, not goat, cabbage)
        if action == "-":
            return (not farmer, wolf, goat, cabbage)

    def value(self, state):
        """we have no good heuristics"""
        return 0


if __name__ == "__main__":
    f = Farmer()
    print(breadth_first_search(f).solution())
