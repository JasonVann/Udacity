import doctest

def bridge_problem2(here):
    "Find the fastest (least path cost) path to the goal in the bridge problem."
    here = frozenset(here) | frozenset(['light'])
    explored = set() # set of states we have visited
    # State will be a (people_here, people_there)
    # E.g. ({1, 2, 5, 10, 'light'}, {})
    frontier = [ [(here, frozenset())] ] # ordered list of paths we have blazed
    while frontier:
        path = frontier.pop(0)
        here1, there1 = state1 = final_state(path)
        if not here1 or (len(here1) == 1 and 'light' in here1):
            return path
        explored.add(state1)
        pcost = path_cost(path)
        for (state, action) in bsuccessors2(state1).items():
            if state not in explored:
                total_cost = pcost + bcost(action)
                path2 = path + [(action, total_cost), state]
                add_to_frontier(frontier, path2)
    return []

bridge_problem = bridge_problem2

def final_state(path):
    return path[-1]

def path_cost(path):
    """The total cost of a path (which is stored in a tuple
    with the final action."""
    # path = [state, (action, total_cost), state, ... ]
    if len(path) < 2:
        return 0
    else:
        return path[-2][-1]

def bcost(action):
    """Returns the cost (a number) of an action in the
    bridge problem."""
    # An action is an (a, b, arrow) tuple; a and b are
    # times; arrow is a string.
    a, b, arrow = action
    return max(a, b)

def add_to_frontier(frontier, path):
    "Add path to frontier, replacing costlier path if there is one."
    # (This could be done more efficiently)
    # Find if there is an old path to the final state of this path.
    old = None
    for i, p in enumerate(frontier):
        if final_state(p) == final_state(path):
            old = i
            break
    if old is not None and path_cost(frontier[old]) < path_cost(path):
        return # Old path was better; do nothing
    elif old is not None:
        del frontier[old] # Old path was worse; delete it
    ## Now add the new path and re-sort
    frontier.append(path)
    frontier.sort(key = path_cost)

def bsuccessors2(state):
    """Return a dict of {state:action} pairs.  A state is a (here, there) tuple,
    where here and there are frozensets of people (indicated by their times) and/or
    the light."""
    here, there = state
    if 'light' in here:
        return dict(((here  - frozenset([a, b, 'light']),
                      there | frozenset([a, b, 'light'])),
                     (a, b, '->'))
                    for a in here if a is not 'light'
                    for b in here if b is not 'light')
    else:
        return dict(((here  | frozenset([a, b, 'light']),
                      there - frozenset([a, b, 'light'])),
                     (a, b, '<-'))
                    for a in there if a is not 'light'
                    for b in there if b is not 'light')

def path_states(path):
    "Return a list of states in this path."
    return path[::2]

def path_actions(path):
    "Return a list of actions in this path."
    return path[1::2]

def test():
    here1 = frozenset([1, 'light'])
    there1 = frozenset([])

    here2 = frozenset([1, 2, 'light'])
    there2 = frozenset([3])

    assert bsuccessors2((here1, there1)) == {
            (frozenset([]), frozenset([1, 'light'])): (1, 1, '->')}
    assert bsuccessors2((here2, there2)) == {
            (frozenset([1]), frozenset(['light', 2, 3])): (2, 2, '->'),
            (frozenset([2]), frozenset([1, 3, 'light'])): (1, 1, '->'),
            (frozenset([]), frozenset([1, 2, 3, 'light'])): (2, 1, '->')}

    assert bsuccessors2((frozenset([1, 'light']), frozenset([]))) == {
        (frozenset([]), frozenset([1, 'light'])): (1, 1, '->')}

    assert bsuccessors2((frozenset([]), frozenset([2, 'light']))) == {
                (frozenset([2, 'light']), frozenset([])): (2, 2, '<-')}
    assert bsuccessors2((frozenset([1, 2, 5, 10, 'light']), frozenset([]))) == {
                (frozenset([1, 10]), frozenset(['light', 2, 5])): (5, 2, '->'),
                (frozenset([10, 5]), frozenset([1, 2, 'light'])): (2, 1, '->'),
                (frozenset([1, 2, 10]), frozenset(['light', 5])): (5, 5, '->'),
                (frozenset([1, 2]), frozenset(['light', 10, 5])): (5, 10, '->'),
                (frozenset([1, 10, 5]), frozenset(['light', 2])): (2, 2, '->'),
                (frozenset([2, 5]), frozenset([1, 10, 'light'])): (10, 1, '->'),
                (frozenset([1, 2, 5]), frozenset(['light', 10])): (10, 10, '->'),
                (frozenset([1, 5]), frozenset(['light', 2, 10])): (10, 2, '->'),
                (frozenset([2, 10]), frozenset([1, 5, 'light'])): (5, 1, '->'),
                (frozenset([2, 10, 5]), frozenset([1, 'light'])): (1, 1, '->')}

    assert path_cost(('fake_state1', ((2, 5, '->'), 5), 'fake_state2')) == 5
    assert path_cost(('fs1', ((2, 1, '->'), 2), 'fs2', ((3, 4, '<-'), 6), 'fs3')) == 6
    assert bcost((4, 2, '->'), ) == 4
    assert bcost((3, 10, '<-'), ) == 10

    assert path_cost(bridge_problem(frozenset((1, 2), ))) == 2
    assert path_cost(bridge_problem(frozenset((1, 2, 5, 10), ))) == 17

    testpath = [(frozenset([1, 10]), frozenset(['light', 2, 5]), 5), # state 1
                (5, 2, '->'),                                        # action 1
                (frozenset([10, 5]), frozenset([1, 2, 'light']), 2), # state 2
                (2, 1, '->'),                                        # action 2
                (frozenset([1, 2, 10]), frozenset(['light', 5]), 5),
                (5, 5, '->'),
                (frozenset([1, 2]), frozenset(['light', 10, 5]), 10),
                (5, 10, '->'),
                (frozenset([1, 10, 5]), frozenset(['light', 2]), 2),
                (2, 2, '->'),
                (frozenset([2, 5]), frozenset([1, 10, 'light']), 10),
                (10, 1, '->'),
                (frozenset([1, 2, 5]), frozenset(['light', 10]), 10),
                (10, 10, '->'),
                (frozenset([1, 5]), frozenset(['light', 2, 10]), 10),
                (10, 2, '->'),
                (frozenset([2, 10]), frozenset([1, 5, 'light']), 5),
                (5, 1, '->'),
                (frozenset([2, 10, 5]), frozenset([1, 'light']), 1),
                (1, 1, '->')]
    assert path_states(testpath) == [(frozenset([1, 10]), frozenset(['light', 2, 5]), 5), # state 1
                (frozenset([10, 5]), frozenset([1, 2, 'light']), 2), # state 2
                (frozenset([1, 2, 10]), frozenset(['light', 5]), 5),
                (frozenset([1, 2]), frozenset(['light', 10, 5]), 10),
                (frozenset([1, 10, 5]), frozenset(['light', 2]), 2),
                (frozenset([2, 5]), frozenset([1, 10, 'light']), 10),
                (frozenset([1, 2, 5]), frozenset(['light', 10]), 10),
                (frozenset([1, 5]), frozenset(['light', 2, 10]), 10),
                (frozenset([2, 10]), frozenset([1, 5, 'light']), 5),
                (frozenset([2, 10, 5]), frozenset([1, 'light']), 1)]
    assert path_actions(testpath) == [(5, 2, '->'), # action 1
                                      (2, 1, '->'), # action 2
                                      (5, 5, '->'),
                                      (5, 10, '->'),
                                      (2, 2, '->'),
                                      (10, 1, '->'),
                                      (10, 10, '->'),
                                      (10, 2, '->'),
                                      (5, 1, '->'),
                                      (1, 1, '->')]

    return 'tests pass'

class TestBridge: """
>>> path_cost(bridge_problem([1,2,5,10]))
17

## There are two equally good solutions
>>> S1 = [((2, 1, '->'), 2), ((1, 1, '<-'), 3), ((5, 10, '->'), 13), ((2, 2, '<-'), 15), ((2, 1, '->'), 17)]

>>> S2 = [((2, 1, '->'), 2), ((2, 2, '<-'), 4), ((5, 10, '->'), 14), ((1, 1, '<-'), 15), ((2, 1, '->'), 17)]
>>> path_actions(bridge_problem([1,2,5,10])) in (S1, S2)
True

## Try some other problems
>>> path_actions(bridge_problem([1,2,5,10,15,20]))
[((2, 1, '->'), 2), ((1, 1, '<-'), 3), ((5, 10, '->'), 13), ((2, 2, '<-'), 15), ((2, 1, '->'), 17), ((1, 1, '<-'), 18), ((15, 20, '->'), 38), ((2, 2, '<-'), 40), ((2, 1, '->'), 42)]

>>> path_actions(bridge_problem([1,2,4,8,16,32]))
[((2, 1, '->'), 2), ((1, 1, '<-'), 3), ((8, 4, '->'), 11), ((2, 2, '<-'), 13), ((1, 2, '->'), 15), ((1, 1, '<-'), 16), ((16, 32, '->'), 48), ((2, 2, '<-'), 50), ((2, 1, '->'), 52)]

>>> [path_cost(bridge_problem([1,2,4,8,16][:N])) for N in range(6)]
[0, 1, 2, 7, 15, 28]

>>> [path_cost(bridge_problem([1,1,2,3,5,8,13,21][:N])) for N in range(8)]
[0, 1, 1, 2, 6, 12, 19, 30]

# http://en.wikipedia.org/wiki/Bridge_and_torch_problem
>>> path_actions(bridge_problem([1,2,5,8]))
[((2, 1, '->'), 2), ((1, 1, '<-'), 3), ((5, 8, '->'), 11), ((2, 2, '<-'), 13), ((2, 1, '->'), 15)]

>>> path_cost(bridge_problem([1,2,5,8]))
15

>>> path_cost(bridge_problem([5,10,20,25]))
60
"""

print(test())
print(doctest.testmod())
pour.py

import doctest

def pour_problem(X, Y, goal, start = (0, 0)):
    """X and Y are the capacity of glasses; (x,y) is current fill levels and
    represent a state. The goal is a level that can be in either glass. Start at
    start state and follow successors until we reach the goal. Keep track of
    frontier and previously explored; fail when no frontier."""
    if goal in start:
        return [start]
    explored = set() # set the states we have visited
    frontier = [ [start] ] # ordered list of paths we have blazed
    while frontier:
        path = frontier.pop(0)
        (x, y) = path[-1] # Last state in the first path of the frontier
        for (state, action) in successors(x, y, X, Y).items():
            if state not in explored:
                explored.add(state)
                path2 = path + [action, state]
                if goal in state:
                    return path2
                else:
                    frontier.append(path2)
    return Fail
Fail = []

def successors(x, y, X, Y):
    """Return a dict of {state:action} pairs describing what can be reached from
    the (x, y) state and how."""
    assert x <= X and y <= Y ## (x, y) is glass levels; X and Y are glass sizes
    return {((0, y+x) if y+x <= Y else (x-(Y-y), y+(Y-y))): 'X->Y',
            ((x+y, 0) if x+y <= X else (x+(X-x), y-(X-x))): 'X<-Y',
            (X, y): 'fill X',
            (x, Y): 'fill Y',
            (0, y): 'empty X',
            (x, 0): 'empty Y'
            }

class Test:
    """
    >>> successors(0, 0, 4, 9)
    {(0, 9): 'fill Y', (0, 0): 'empty Y', (4, 0): 'fill X'}

    >>> successors(3, 5, 4, 9)
    {(4, 5): 'fill X', (4, 4): 'X<-Y', (3, 0): 'empty Y', (3, 9): 'fill Y', (0, 5): 'empty X', (0, 8): 'X->Y'}

    >>> successors(3, 7, 4, 9)
    {(4, 7): 'fill X', (4, 6): 'X<-Y', (3, 0): 'empty Y', (0, 7): 'empty X', (3, 9): 'fill Y', (1, 9): 'X->Y'}

    >>> pour_problem(4, 9, 6)
    [(0, 0), 'fill Y', (0, 9), 'X<-Y', (4, 5), 'empty X', (0, 5), 'X<-Y', (4, 1), 'empty X', (0, 1), 'X<-Y', (1, 0), 'fill Y', (1, 9), 'X<-Y', (4, 6)]

    ## What problem, with X, Y, and goal < 10 has the longest solution?
    ## Answer: pour_problem(7, 9, 8) with 14 steps.

    >>> def num_actions(triplet): X, Y, goal = triplet; return len(pour_problem(X, Y, goal)) / 2

    >>> def hardness(triplet): X, Y, goal = triplet; return num_actions((X, Y, goal)) - max(X, Y)
    >>> max([(X, Y, goal) for X in range(1, 10) for Y in range(1, 10)
    ...                   for goal in range(1, max(X, Y))], key = num_actions)
    (7, 9, 8)

    >>> max([(X, Y, goal) for X in range(1, 10) for Y in range(1, 10)
    ...                   for goal in range(1, max(X, Y))], key = hardness)
    (7, 9, 8)

    >>> pour_problem(7, 9, 8)
    [(0, 0), 'fill Y', (0, 9), 'X<-Y', (7, 2), 'empty X', (0, 2), 'X<-Y', (2, 0), 'fill Y', (2, 9), 'X<-Y', (7, 4), 'empty X', (0, 4), 'X<-Y', (4, 0), 'fill Y', (4, 9), 'X<-Y', (7, 6), 'empty X', (0, 6), 'X<-Y', (6, 0), 'fill Y', (6, 9), 'X<-Y', (7, 8)]
    """

print(doctest.testmod())
# TestResults(failed=0, attempted=9)
