#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given n glasses standing upright at the beginning.
In one step any k of the glasses need to be turned over.
Our aim is to reach the state in which all glasses are standing downright.
"""

from search import Problem, uniform_cost_search

TIME=[1,2,5,10]

class Torch(Problem):
    "Turn glasses"
    def __init__(self):
        self.initial = (False, False, False, False, False)
        self.goal =    (True, True, True, True, True)

    def actions(self, state):
        acts = []
        acts.extend(i for i in range(4) if state[4]==state[i])
        acts.extend((i,j) for i in range(4) for j in range(4)\
                    if i<j and state[i]==state[j] and state[j]==state[4])
        return acts

    def result(self, state, action):
        ps = list(state)
        if isinstance(action,int):
            ps[action] = not ps[action]
        else:
            ps[action[0]] = not ps[action[0]]
            ps[action[1]] = not ps[action[1]]
        ps[4] = not ps[4]
        return tuple(ps)

    def path_cost(self, c, state1, action, state2):
        if isinstance(action, int):
            return c+TIME[action]
        else:
            return c+TIME[action[1]]

    def value(self, state):
        """we have no good heuristics"""
        return 0

if __name__ == "__main__":
    t = Torch()
    print(uniform_cost_search(t).solution())
