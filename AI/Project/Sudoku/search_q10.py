from utils import *

def search(values):
    "Using depth-first search and propagation, create a search tree and solve the sudoku."
    # First, reduce the puzzle using the previous function
    #print(boxes)
    #print(values['C1'])
    res = reduce_puzzle(values)
    
    if not res:
        # No solution
        return False
    
    #display(values)
    #print()
    
    # Choose one of the unfilled squares with the fewest possibilities
    min_box = None
    for box in boxes:
        if len(values[box]) > 1:
            if min_box == None or len(values[min_box]) > len(values[box]):
                min_box = box
    
    if min_box == None:
        if check_solved(values):
            # Then the sudoku is already fully solved
            return values
        return False
        
    # Now use recursion to solve each one of the resulting sudokus, and if one returns a value (not False), return that answer!
    
    import copy
    cand = values[min_box]
    for digit in cand:
        #values0 = copy.deepcopy(values)
        values0 = values.copy()
        values0[min_box] = digit
        res = search(values0)
        if not res:
            continue
            
        if check_solved(res):
            return res
            
    
def check_solved(values):
    solved = [box for box in boxes if len(values[box]) == 1]
    return len(solved) == 81
