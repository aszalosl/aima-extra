#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given n glasses standing upright at the beginning.
In one step any k of the glasses need to be turned over.
Our aim is to reach the state in which all glasses are standing downright.
"""

from search import Problem, breadth_first_search
from itertools import combinations


class Glasses(Problem):
    "Turn glasses"
    def __init__(self, n, k):
        self.initial = tuple([False]*n)
        self.goal =    tuple([True]*n)
        self.turn = k

    def actions(self, state):
        return combinations(range(len(state)), self.turn)

    def result(self, state, action):
        glasses = list(state)
        turn = list(action)
        for i in turn:
            glasses[i] = not glasses[i]
        return tuple(glasses)

    def value(self, state):
        """we have no good heuristics"""
        return 0


if __name__ == "__main__":
    g = Glasses(6,2)
    print(breadth_first_search(g).solution())
