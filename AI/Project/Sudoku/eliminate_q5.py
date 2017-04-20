from utils import *

def eliminate(values):
    """Eliminate values from peers of each box with a single value.

    Go through all the boxes, and whenever there is a box with a single value,
    eliminate this value from the set of values of all its peers.

    Args:
        values: Sudoku in dictionary form.
    Returns:
        Resulting Sudoku in dictionary form after eliminating values.
    """
    import copy
    values2 = copy.deepcopy(values)
    changed = True
    '''
    print(values)
    print(peers)
    return
    '''
    
    #while changed:
    changed = False
    for k, v in values2.items():
        if len(v) == 1:
            for peer in peers[k]:
                if v in values[peer]:
                    values[peer] = values[peer].replace(v,'')
                    changed = True
            
    #'''            
    return values
    
