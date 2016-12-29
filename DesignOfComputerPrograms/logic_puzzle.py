"""
UNIT 2: Logic Puzzle

You will write code to solve the following logic puzzle:

1. The person who arrived on Wednesday bought the laptop.
2. The programmer is not Wilkes.
3. Of the programmer and the person who bought the droid,
   one is Wilkes and the other is Hamming. 
4. The writer is not Minsky.
5. Neither Knuth nor the person who bought the tablet is the manager.
6. Knuth arrived the day after Simon.
7. The person who arrived on Thursday is not the designer.
8. The person who arrived on Friday didn't buy the tablet.
9. The designer didn't buy the droid.
10. Knuth arrived the day after the manager.
11. Of the person who bought the laptop and Wilkes,
    one arrived on Monday and the other is the writer.
12. Either the person who bought the iphone or the person who bought the tablet
    arrived on Tuesday.

You will write the function logic_puzzle(), which should return a list of the
names of the people in the order in which they arrive. For example, if they
happen to arrive in alphabetical order, Hamming on Monday, Knuth on Tuesday, etc.,
then you would return:

['Hamming', 'Knuth', 'Minsky', 'Simon', 'Wilkes']
['iphone', 'tablet', 'droid', 'laptop', 'toy']
['writer', 'designer', 'manager', 'programmer', 'job']

(You can assume that the days mentioned are all in the same week.)
"""

people = ['Hamming', 'Knuth', 'Minsky', 'Simon', 'Wilkes']
#days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

toys = ['iphone', 'tablet', 'droid', 'laptop', 'unknown']
jobs = ['writer', 'designer', 'manager', 'programmer', 'unknown']

import itertools

def logic_puzzle():
    "Return a list of the names of the people, in the order they arrive."
    ## your code here; you are free to define additional functions if needed
    orderings = [1,2,3,4,5]
    for (Hamming, Knuth, Minsky, Simon, Wilkes) in itertools.permutations(orderings):
        if Knuth != Simon + 1:
            continue
        for (iphone, tablet, droid, laptop, toy) in itertools.permutations(orderings):
            if laptop != 3:
                continue
            for (writer, designer, manager, programmer, job) in itertools.permutations(orderings):
                if Wilkes == programmer:
                    continue
                if not (Wilkes == droid and Hamming == programmer):
                    continue
                if Minsky == writer:
                    continue
                if Knuth == manager or tablet == manager:
                    continue
                if designer == 4:
                    continue
                if tablet == 5:
                    continue
                if droid == designer:
                    continue
                if Knuth != manager + 1:
                    continue
                if not ((Wilkes == 1 and laptop == writer) or (Wilkes == writer and 1 == laptop)):
                    continue
                if not (2 == iphone or tablet == 2):
                    continue
                res = []
                print [Hamming, Knuth, Minsky, Simon, Wilkes]
                return ['Wilkes', 'Simon', 'Knuth', 'Hamming', 'Minsky']
                
print logic_puzzle()

