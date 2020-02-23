#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Three missionaries and three cannibals must cross a river using a boat
which can carry at most two people, under the constraint that,
for both banks, if there are missionaries present on the bank,
they cannot be outnumbered by cannibals (if they were, the
cannibals would eat the missionaries).
The boat cannot cross the river by itself with no people on board."""

from search import Problem, breadth_first_search
from collections import namedtuple
State = namedtuple("State", ["ml", "cl", "boat_on_left", "mr", "cr"])

class Cannibal(Problem):
    "Missionaries and cannibals"
    def __init__(self, size):
        """We use numbers to show number of missionaries and cannibals
        at both banks, and a boolean to show the position of the boat"""
        self.initial = (size, size, False, 0, 0)
        self.goal = (0, 0, True, size, size)

    def actions(self, state):
        m_l, c_l, boat, m_r, c_r = state
        acts = []
        if boat:  # from right to left
            if (m_r-2 >= c_r or m_r == 2) and m_l+2 >= c_l:
                acts.append("<mm")
            if (m_r-1 >= c_r or m_r == 1) and m_l+1 >= c_l:
                acts.append("<m")
            if m_r >= c_r and m_l >= c_l and c_r>=1:
                acts.append("<mc")
            if c_r >= 2 and (m_l == 0 or m_l >= c_l+2):
                acts.append("<cc")
            if c_r >= 1 and (m_l == 0 or m_l >= c_l+1):
                acts.append("<c")
        else:     # from left to rigth
            if (m_l-2 >= c_l or m_l == 2) and m_r+2 >= c_r:
                acts.append("mm>")
            if (m_l-1 >= c_l or m_l == 1) and m_r+1 >= c_r:
                acts.append("m>")
            if m_l >= c_l and m_r >= c_r and c_l>=1:
                acts.append("mc>")
            if c_l >= 2 and (m_r == 0 or m_r >= c_r+2):
                acts.append("cc>")
            if c_l >= 1 and (m_r == 0 or m_r >= c_r+1):
                acts.append("c>")
        return acts

    def result(self, state, action):
        m_l, c_l, boat, m_r, c_r = state
        d = {
          "<mm": (m_l+2, c_l, False, m_r-2, c_r),
          "<m":  (m_l+1, c_l, False, m_r-1, c_r),
          "<mc": (m_l+1, c_l+1, False, m_r-1, c_r-1),
          "<cc": (m_l, c_l+2, False, m_r, c_r-2),
          "<c":  (m_l, c_l+1, False, m_r, c_r-1),
          "mm>": (m_l-2, c_l, True, m_r+2, c_r),
          "m>":  (m_l-1, c_l, True, m_r+1, c_r),
          "mc>": (m_l-1, c_l-1, True, m_r+1, c_r+1),
          "cc>": (m_l, c_l-2, True, m_r, c_r+2),
          "c>":  (m_l, c_l-1, True, m_r, c_r+1)}
        return d[action]

    def value(self, state):
        """we have no good heuristics"""
        return 0


if __name__ == "__main__":
    c3 = Cannibal(3)
    print(breadth_first_search(c3).solution())
    c4 = Cannibal(4)
    s4 = breadth_first_search(c4)
    if s4: 
        print(s4.solution())
    else:
        print("No solution for n=4")  
    c5 = Cannibal(5)
    s5 = breadth_first_search(c5)
    if s5: 
        print(s5.solution())
    else:
        print("No solution for n=5")  

