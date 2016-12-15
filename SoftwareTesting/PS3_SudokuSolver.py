# CHALLENGE PROBLEM: 
#
# Use your check_sudoku function as the basis for solve_sudoku(): a
# function that takes a partially-completed Sudoku grid and replaces
# each 0 cell with an integer in the range 1..9 in such a way that the
# final grid is valid.
#
# There are many ways to cleverly solve a partially-completed Sudoku
# puzzle, but a brute-force recursive solution with backtracking is a
# perfectly good option. The solver should return None for broken
# input, False for inputs that have no valid solutions, and a valid
# 9x9 Sudoku grid containing no 0 elements otherwise. In general, a
# partially-completed Sudoku grid does not have a unique solution. You
# should just return some member of the set of solutions.
#
# A solve_sudoku() in this style can be implemented in about 16 lines
# without making any particular effort to write concise code.

# solve_sudoku should return None
ill_formed = [[5,3,4,6,7,8,9,1,2],
              [6,7,2,1,9,5,3,4,8],
              [1,9,8,3,4,2,5,6,7],
              [8,5,9,7,6,1,4,2,3],
              [4,2,6,8,5,3,7,9],  # <---
              [7,1,3,9,2,4,8,5,6],
              [9,6,1,5,3,7,2,8,4],
              [2,8,7,4,1,9,6,3,5],
              [3,4,5,2,8,6,1,7,9]]

# solve_sudoku should return valid unchanged
valid = [[5,3,4,6,7,8,9,1,2],
         [6,7,2,1,9,5,3,4,8],
         [1,9,8,3,4,2,5,6,7],
         [8,5,9,7,6,1,4,2,3],
         [4,2,6,8,5,3,7,9,1],
         [7,1,3,9,2,4,8,5,6],
         [9,6,1,5,3,7,2,8,4],
         [2,8,7,4,1,9,6,3,5],
         [3,4,5,2,8,6,1,7,9]]

# solve_sudoku should return False
invalid = [[5,3,4,6,7,8,9,1,2],
           [6,7,2,1,9,5,3,4,8],
           [1,9,8,3,8,2,5,6,7],
           [8,5,9,7,6,1,4,2,3],
           [4,2,6,8,5,3,7,9,1],
           [7,1,3,9,2,4,8,5,6],
           [9,6,1,5,3,7,2,8,4],
           [2,8,7,4,1,9,6,3,5],
           [3,4,5,2,8,6,1,7,9]]

# solve_sudoku should return a 
# sudoku grid which passes a 
# sudoku checker. There may be
# multiple correct grids which 
# can be made from this starting 
# grid.
easy = [[2,9,0,0,0,0,0,7,0],
        [3,0,6,0,0,8,4,0,0],
        [8,0,0,0,4,0,0,0,2],
        [0,2,0,0,3,1,0,0,7],
        [0,0,0,0,8,0,0,0,0],
        [1,0,0,9,5,0,0,6,0],
        [7,0,0,0,9,0,0,0,1],
        [0,0,1,2,0,0,3,0,6],
        [0,3,0,0,0,0,0,5,9]]

# Note: this may timeout 
# in the Udacity IDE! Try running 
# it locally if you'd like to test 
# your solution with it.
# 
hard = [[1,0,0,0,0,7,0,9,0],
         [0,3,0,0,2,0,0,0,8],
         [0,0,9,6,0,0,5,0,0],
         [0,0,5,3,0,0,9,0,0],
         [0,1,0,0,8,0,0,0,2],
         [6,0,0,0,0,4,0,0,0],
         [3,0,0,0,0,0,0,1,0],
         [0,4,0,0,0,0,0,0,7],
         [0,0,7,0,0,0,3,0,0]]

def check_sudoku(grid):
    # Sanity check
    for i in range(9):
        row = grid[i]
        if len(row) < 9:
            return None
        for j in row:
            if j not in range(0,10):
                return None
    # Then check True/False
    
    for i in range(9):
        row = grid[i]
        for j in range(1,10):
            if row.count(j) > 1:
                return False
        col = []
        for k in range(9):
            col.append(grid[k][i])
        for j in range(1,10):
            if col.count(j) > 1:
                return False
    
    # Then check sub-grid
    for i in range(3):
        for j in range(3):
            sub = []
            for k in range(9):
                sub.append(grid[i*3 + k/3][j*3+k%3])
            #print 131, sub
        for k in range(1,10):
            if sub.count(k) > 1:
                return False
    return True
    
def solve_sudoku (grid):
    ###Your code here.
    res = check_sudoku(grid)
    if not res:
        return res
    solve(grid)
    print 124, grid
    
import time
start_time = time.time()

def solve(board):
    from collections import defaultdict
    import pprint
    dic = defaultdict(list)
    unknown = defaultdict(list)
    d_r = defaultdict(list)
    d_v = defaultdict(list)
    d_sq = defaultdict(list)
    l_board = []
    for i in range(len(board)):
        row = board[i]
        for j in range(len(row)):
            cell = row[j]
            i_sq = 3 * (i / 3) + j / 3
            if cell == 0:
                #unknown.append((i, j))
                d_r[i] += [None]
                d_v[j] += [None]
                #d_sq[i_sq] += [None]
            else:
                val = int(cell)
                dic[val] += [(i, j)]
                d_r[i] += [val]
                d_v[j] += [val]
                d_sq[i_sq] += [val]

    while True:
        found_count = 0
        for i in range(9):
            row = []
            for j in range(9):

                if board[i][j] != 0:
                    row.append(int(board[i][j]))
                else:
                    cell = d_r[i][j]
                    if cell != None:
                        continue
                    all = [x for x in range(1, 10)]
                    false = d_r[i] + d_v[j]
                    i_sq = 3 * (i / 3) + j / 3
                    false += d_sq[i_sq]
                    candidate = list(set(all) - set(false))

                    if len(candidate) == 1:
                        d_r[i][j] = candidate[0]
                        d_v[j][i] = candidate[0]
                        d_sq[i_sq] += candidate
                        found_count += 1

        if found_count == 0:
            break

    #Then find unknown
    has_unknown = False
    for i in range(9):
        row = []
        for j in range(9):
            if board[i][j] == 0 and d_r[i][j] == None:
                all = [x for x in range(1, 10)]
                false = d_r[i] + d_v[j]
                i_sq = 3 * (i / 3) + j / 3
                false += d_sq[i_sq]
                candidate = list(set(all) - set(false))

                if len(candidate) > 1:
                    unknown[len(candidate)] += [[candidate, (i, j)]]
                    row.append(list(candidate))

    # Then backtrack
    guess = []
    #return

    back_track_count = 0
    m = 2
    n = 0
    i_sel = 0
    while True:

        k = unknown.keys()
        if len(k) == 0:
            break

        if n >= len(unknown[m]):
            n = 0
            m += 1
            while m not in unknown.keys() and m < max(unknown.keys()):
                m += 1
        if m > max(unknown.keys()):
            break

        cand, (i, j) = unknown[m][n]

        i_sq = 3 * (i / 3) + j / 3

        while True:
            found = False
            if i_sel >= len(cand):
                break
            if cand[i_sel] not in d_r[i] and cand[i_sel] not in d_v[j] and cand[i_sel] not in d_sq[i_sq]:
                found = True
                break
            else:
                i_sel += 1
                if i_sel >= len(cand):
                    break
        if found:
            guess.append([cand, (m, n), (i, j), i_sel])
            d_r[i][j] = cand[i_sel]
            d_v[j][i] = cand[i_sel]
            d_sq[i_sq] += [cand[i_sel]]
            i_sel = 0
        else:
            # Conflict, backtrack
            cand, (m, n), (i, j), i_sel = guess.pop()
            back_track_count += 1
            d_r[i][j] = None
            d_v[j][i] = None
            i_sq = 3 * (i / 3) + j / 3
            d_sq[i_sq].remove(cand[i_sel])
            #cand.pop(0)
            i_sel += 1
            continue

        last_check = (m, n)
        n = n + 1

        #break

    #print back_track_count
    for i in range(9):
        row = d_r[i]
        #row = [str(x) for x in row]
        d_r[i] = row

    
    #print d_r
    for i in range(9):
        board[i] = d_r[i]

    #pp = pprint.PrettyPrinter(width = 4, depth=2)
    #pp.pprint(d_r)
    return board
    
def solve0(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                for k in range(9):
                    grid[i][j] = k
                    if check_sudoku(grid):
                        found = False
                        for m in range(9):
                            if 0 in grid[m]:
                                found = True
                        if not found:
                            return
                        break

solve_sudoku(easy)
#print easy
#print time.time() - start_time



