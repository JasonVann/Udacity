# Bonus Practice: Subsets

# This assignment is not graded and we encourage you to experiment. Learning is
# fun!

# Write a procedure that accepts a list as an argument. The procedure should
# print out all of the subsets of that list.

def sub(people, res, cur):
    for i in range(len(people)):
        
        sub(people[i+1:], res, cur[:])
        sub(people[i+1:], res, cur+[people[i]])
    if cur not in res:
        res += [cur]
    return res

def sub(people, res, cur):
    if len(people) >= 1:
        sub(people[1:], res, cur)
        sub(people[1:], res, cur+[people[0]])
    if cur not in res:
        res += [cur]
    return res

def sub(people, res, cur):
    if len(people) >= 1:
        a = sub(people[1:], res, cur)
        b = sub(people[1:], res, cur+[people[0]])
        return a + b
    return [cur]

people = ['a', 'b', 'c']
res = []
print sub(people, res, [])
#print res
        
