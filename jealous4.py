#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Four married couples must cross a river using a boat which can hold at most
two people, subject to the constraint that no woman can be in the presence of
another man unless her husband is also present. The boat cannot cross the river
by itself with no people on board. There is an island in the middle of the
river where the boat may land and leave some of its cargo.
"""

from search import Problem, breadth_first_graph_search

LEFT =   0
ISLAND = 1
RIGHT =  2

def safe_set(s):
    if s & set(['A','B','C','D']) == set():
        return True
    if 'a' in s and 'A' not in s and ('B' in s or 'C' in s or 'D' in s):
        return False
    if 'b' in s and 'B' not in s and ('A' in s or 'C' in s or 'D' in s):
        return False
    if 'c' in s and 'C' not in s and ('A' in s or 'B' in s or 'D' in s):
        return False
    if 'd' in s and 'D' not in s and ('A' in s or 'B' in s or 'C' in s):
        return False
    return True

def safe(source, target, boat):
    return safe_set(boat) and safe_set(source - boat) and \
            safe_set(target | boat)


class Jealous4(Problem):
    "Four married couple"
    def __init__(self):
        """We use sets to show persons on the banks
        and a boolean to show the position of the boat.
        Capital letters denotes the husbands."""
        self.initial = (frozenset(['a','A','b','B','c','C','d','D']),
                        frozenset(), frozenset(), LEFT)
        self.goal =    (frozenset(), frozenset(),
                        frozenset(['a','A','b','B','c','C','d','D']), RIGHT)

    def actions(self, state):
        setL, setI, setR, boat = state
        acts = []
        if boat == RIGHT:  # from right to left
            acts.extend(['L'+p for p in setR if safe(setR, setL, set(p))])
            acts.extend(['I'+p for p in setR if safe(setR, setI, set(p))])
            # pairs
            acts.extend(['L'+p+q for p in setR for q in setR if p<q and \
                         safe(setR, setL, set([p,q]))])
            acts.extend(['I'+p+q for p in setR for q in setR if p<q and \
                         safe(setR, setI, set([p,q]))])
        elif boat == LEFT:     # from left to rigth
            acts.extend(['R'+p for p in setL if safe(setL, setR, set(p))])
            acts.extend(['I'+p for p in setL if safe(setL, setI, set(p))])
            # pairs
            acts.extend(['R'+p+q for p in setL for q in setL if p<q and \
                         safe(setL, setR, set([p,q]))])
            acts.extend(['I'+p+q for p in setL for q in setL if p<q and \
                         safe(setL, setI, set([p,q]))])
        else:
            acts.extend(['R'+p for p in setI if safe(setI, setR, set(p))])
            acts.extend(['L'+p for p in setI if safe(setI, setL, set(p))])
            # pairs
            acts.extend(['R'+p+q for p in setI for q in setI if p<q and \
                         safe(setI, setR, set([p,q]))])
            acts.extend(['L'+p+q for p in setI for q in setI if p<q and \
                         safe(setI, setL, set([p,q]))])
        return acts

    def result(self, state, action):
        setL, setI, setR, boat = state
        if boat == LEFT:
            setS = setL
        elif boat == ISLAND:
            setS = setI
        else:
            setS = setR
        if action[0] == 'L':
            setT = setL
        elif action[0] == 'I':
            setT = setI
        else:
            setT = setR

        p = action[1]
        if len(action) == 2:
            setS2 = frozenset(setS - set(p))
            setT2 = frozenset(setT | set(p))
        else:
            q = action[2]
            setS2 = frozenset(setS - set(p) - set(q))
            setT2 = frozenset(setT | set(p) | set(q))
        if boat == LEFT:
            if action[0] == 'I':
                return (setS2, setT2, setR, ISLAND)
            else:
                return (setS2, setI, setT2, RIGHT)
        elif boat == ISLAND:
            if action[0] == 'L':
                return (setT2, setS2, setR, LEFT)
            else:
                return (setL, setS2, setT2, RIGHT)
        else:
            if action[0] == 'L':
                return (setT2, setI, setS2, LEFT)
            else:
                return (setL, setT2, setS2, ISLAND)

    def value(self, state):
        """we have no good heuristics"""
        return 0


if __name__ == "__main__":
    j = Jealous4()
    print(breadth_first_graph_search(j).solution())
