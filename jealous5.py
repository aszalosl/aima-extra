#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Five married couples must cross a river using a boat which can hold at
most three people, subject to the constraint that no woman can be in the
presence of another man unless her husband is also present.
The boat cannot cross the river by itself with no people on board.
"""


from search import Problem, breadth_first_graph_search

def safe_set(s):
    if s & set(['A','B','C', 'D', 'E']) == set():
        return True
    if 'a' in s and 'A' not in s and ('B' in s or 'C' in s or 'D' in s or 'E' in s):
        return False
    if 'b' in s and 'B' not in s and ('A' in s or 'C' in s or 'D' in s or 'E' in s):
        return False
    if 'c' in s and 'C' not in s and ('A' in s or 'B' in s or 'D' in s or 'E' in s):
        return False
    if 'd' in s and 'D' not in s and ('A' in s or 'B' in s or 'C' in s or 'E' in s):
        return False
    if 'e' in s and 'E' not in s and ('A' in s or 'B' in s or 'C' in s or 'D' in s):
        return False
    return True

def safe(source, target, boat):
    return safe_set(boat) and safe_set(source - boat) and \
            safe_set(target | boat)


class Jealous5(Problem):
    "Five married couple"
    def __init__(self):
        """We use sets to show persons on the banks
        and a boolean to show the position of the boat
        Capital letters denotes the husbands.
        """
        everybody = frozenset(["a","A","b","B", "c", "C", "d", "D", "e", "E"])
        self.initial = (everybody, frozenset(), False)
        self.goal =    (frozenset(), everybody, True)

    def actions(self, state):
        setL, setR, boat = state
        acts = []
        if boat:  # from right to left
            acts.extend(['<'+p for p in setR if safe(setR, setL, set(p))])
            # pairs
            acts.extend(['<'+p+q for p in setR for q in setR if p<q and \
                         safe(setR, setL, set([p,q]))])
            acts.extend(['<'+p+q+r for p in setR for q in setR for r in setR if p<q and q<r and \
                         safe(setR, setL, set([p,q,r]))])
        else:     # from left to rigth
            acts.extend([p+'>' for p in setL if safe(setL, setR, set(p))])
            # pairs
            acts.extend([p+q+'>' for p in setL for q in setL if p<q and \
                         safe(setL, setR, set([p,q]))])
            acts.extend([p+q+r+'>' for p in setL for q in setL for r in setL if p<q and q<r and \
                         safe(setL, setR, set([p,q,r]))])
        return acts

    def result(self, state, action):
        setL, setR, boat = state
        if action[0] == '<':     # from right to left
            if len(action) == 2:
                p = action[1]
                setL2 = setL | set(p)
                setR2 = setR - set(p)
                return (frozenset(setL2), frozenset(setR2), False)
            if len(action) == 3:
                p = action[1]
                q = action[2]
                setL2 = setL | set(p) | set(q)
                setR2 = setR - set(p) - set(q)
                return (frozenset(setL2), frozenset(setR2), False)
            else:
                p = action[1]
                q = action[2]
                r = action[3]
                setL2 = setL | set(p) | set(q) | set(r)
                setR2 = setR - set(p) - set(q) - set(r)
                return (frozenset(setL2), frozenset(setR2), False)
        else:     # from left to right
            if len(action) == 2:
                p = action[0]
                setL2 = setL - set(p)
                setR2 = setR | set(p)
                return (frozenset(setL2), frozenset(setR2), True)
            if len(action) == 3:
                p = action[0]
                q = action[1]
                setL2 = setL - set(p) - set(q)
                setR2 = setR | set(p) | set(q)
                return (frozenset(setL2), frozenset(setR2), True)
            else:
                p = action[0]
                q = action[1]
                r = action[2]
                setL2 = setL - set(p) - set(q) - set(r)
                setR2 = setR | set(p) | set(q) | set(r)
                return (frozenset(setL2), frozenset(setR2), True)

    def value(self, state):
        """we have no good heuristics"""
        return 0


if __name__ == "__main__":
    j = Jealous5()
    print(breadth_first_graph_search(j).solution())
