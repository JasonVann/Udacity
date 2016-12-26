# --------------
# User Instructions
#
# Write a function, longest_subpalindrome_slice(text) that takes 
# a string as input and returns the i and j indices that 
# correspond to the beginning and end indices of the longest 
# palindrome in the string. 
#
# Grading Notes:
# 
# You will only be marked correct if your function runs 
# efficiently enough. We will be measuring efficency by counting
# the number of times you access each string. That count must be
# below a certain threshold to be marked correct.
#
# Please do not use regular expressions to solve this quiz!

def longest_subpalindrome_slice(text):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    # Your code here
    n = len(text)
    m = n/2
    res = (0,0)
    text = text.upper()
    for i in range(0, n, 1):
        temp = None
        if i + 1 < n and text[i] == text[i+1] and text[i-1] != text[i]:
            temp = (i, i+2)
        for j in range(0, i+1, 1):
            #print 30, i, j, text[i-j], text[i+j]
            if i + j >= n or text[i-j] != text[i+j]:
                j -= 1
                break
        if temp == None:
            temp = (i-j, i+j+1)
        if res[1] - res[0] < temp[1] - temp[0]:
            res = temp
        #print 37, i, res, text[res[0]:res[1]], text
    return res
    
def test():
    L = longest_subpalindrome_slice
    
    assert L('racecar') == (0, 7)
    assert L('Racecar') == (0, 7)
    assert L('RacecarX') == (0, 7)
    
    assert L('Race carr') == (7, 9)
    assert L('') == (0, 0)
    assert L('something rac e car going') == (8,21)
    
    assert L('xxxxx') == (0, 5)
    assert L('Mad am I ma dam.') == (0, 15)
    return 'tests pass'

print test()
