from utils import *

def only_choice(values):
    """Finalize all values that are the only choice for a unit.

    Go through all the units, and whenever there is a unit with a value
    that only fits in one box, assign the value to this box.

    Input: Sudoku in dictionary form.
    Output: Resulting Sudoku in dictionary form after filling in only choices.
    """
    # TODO: Implement only choice strategy here
    
    #print(units)
    '''
    box = 'E3'
    print(values[box])
    print(peers[box])
    print(units[box])
    #display(values)
    print()
    '''
    
    #return only_choice2(values)
    
    for box in values:
        if len(values[box]) == 1:
            continue
        for unit in units[box]:
            peer_nums = [values[peer] for peer in unit if peer != box]
            peer_nums = ''.join(peer_nums)
            diff = set(values[box]) - set(peer_nums)
                
            #print(37, box, values[box], peer_nums, diff)
            if len(diff) == 1:
                values[box] = diff.pop()
                found = True
                break
               
    return values
    
def only_choice2(values):
    # a straightforward method
    
    for box in values:
        if len(values[box]) == 1:
            continue
        for num in values[box]:
            for unit in units[box]:
                found = False
                for peer in unit:
                    if peer == box:
                        continue
                    
                    if num in values[peer]:
                        #print(30, box, num, values[box], peer, values[peer], unit, found)
                        found = True
                        break
                if not found:
                    values[box] = num
                    break
    return values
                
        
   
   
