#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
You need to equally distribute 12 liters of vodka in a bucket between two
Russian peasants. They have two bottles with capacity of 8 and 5 liters.
"""

from search import Problem, breadth_first_graph_search

class Vodka(Problem):
    "Turn glasses"
    def __init__(self):
        self.initial = (12,0,0)
        self.goal =    (6,6,0)

    def actions(self, state):
        acts = []
        twelve, eight, five = state
        if twelve > 0 and eight < 8:
            acts.append("te")
        if twelve > 0 and five < 5:
            acts.append("tf")
        if eight > 0 and five < 5:
            acts.append("ef")
        if eight > 0 and twelve < 12:
            acts.append("et")
        if five > 0 and eight < 8:
            acts.append("fe")
        if five > 0 and twelve < 12:
            acts.append("ft")
        return acts

    def result(self, state, action):
        twelve, eight, five = state
        if action == "te":
            m = min(twelve, 8-eight)
            return (twelve-m, eight+m, five)
        if action == "tf":
            m = min(twelve, 5-five)
            return (twelve-m, eight, five+m)
        if action == "et":
            m = min(eight, 12-twelve)
            return (twelve+m, eight-m, five)
        if action == "ef":
            m = min(eight, 5-five)
            return (twelve, eight-m, five+m)
        if action == "ft":
            m = min(five, 12-twelve)
            return (twelve+m, eight, five-m)
        if action == "fe":
            m = min(five, 8-eight)
            return (twelve, eight+m, five-m)

    def value(self, state):
        """we have no good heuristics"""
        return 0


if __name__ == "__main__":
    v = Vodka()
    print(breadth_first_graph_search(v).solution())
