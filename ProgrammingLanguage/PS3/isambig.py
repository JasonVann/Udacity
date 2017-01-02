# Detecting Ambiguity 
#
# A grammar is ambiguous if there exists a string in the language of that
# grammar that has two (or more) parse trees. Equivalently, a grammar is
# ambiguous if there are two (or more) different sequences of rewrite rules
# that arrive at the same final string.
#
# Ambiguity is a critical concept in natural languages and in programming
# languages. If we are not careful, our formal grammars for languages like
# JavaScript will have ambiguity. 
#
# In this problem you will write a procedure isambig(grammar,start,tokens)
# that takes as input a grammar with a finite number of possible
# derivations and a string and returns True (the value True, not the string
# "True") if those tokens demonstrate that the grammar is ambiguous
# starting from that start symbol (i.e., because two different sequences of
# rewrite rules can arrive at those tokens). 
#
# For example: 
#
# grammar1 = [                  # Rule Number
#       ("S", [ "P", ] ),       # 0
#       ("S", [ "a", "Q", ]) ,  # 1
#       ("P", [ "a", "T"]),     # 2
#       ("P", [ "c" ]),         # 3
#       ("Q", [ "b" ]),         # 4
#       ("T", [ "b" ]),         # 5
#       ] 
#
# In this grammar, the tokens ["a", "b"] do demonstrate that the
# grammar is ambiguous because there are two difference sequences of
# rewrite rules to obtain them:  
#
#       S  --0->  P  --2->  a T  --5->  a b 
#
#       S  --1->  a Q  --4->  a b 
#
# (I have written the number of the rule used inside the arrow for
# clarity.) The two sequences are [0,2,5] and [1,4]. 
#
# However, the tokens ["c"] do _not_ demonstrate that the grammar is
# ambiguous, because there is only one derivation for it:
#
#       S  --0->  P  --3->  c
#
# So even though the grammar is ambiguous, the tokens ["c"] do not
# demonstrate that: there is only one sequence [0,3]. 
#
# Important Assumption: In this problem the grammar given to you will
# always have a finite number of possible derivations. So only a
# finite set of strings will be in the language of the grammar. (You could
# test this with something like cfginfinite, so we'll just assume it.) 
#
# Hint 1: Consider something like "expand" from the end of the Unit, but
# instead of just enumerating utterances, enumerate (utterance,derivation)
# pairs. For a derivation, you might use a list of the rule indexes as we
# did in the example above. 
#
# Hint 2: Because the grammar has only a finite number of derivations, you
# can just keep enumerating new (utterance,derivation) pairs until you 
# cannot find any that are not already enumerated. 

def isambig(grammar, start, utterance):
    # Write your code here!
    cands = [rule for rule in grammar if rule[0] == start]
    res = []
    visited = [[start]]
    for rule in cands:
        # print 93, rule, cands, utterance
        path = [rule]
        (path, done) = match(rule, grammar, utterance, path, res)
        if path:
            print 94, 'Found', rule, path, res
    #print 100, res, len(res)
    return len(res) > 1


def match(rule, grammar, utterance, path, res):
    done = False
    left = [a[0] for a in grammar]
    if len(rule[1]) == 0:
        if len(utterance) == 0:
            if path not in res:
                res += [path]
        else:
            return (path, False)
        return (path, True)

    # print 103, rule, utterance
    for s in rule[1]:
        # print 104, s, rule, utterance
        if len(utterance) == 0:
            return (None, False)
        if s == utterance[0]:
            (path, done) = match((rule[0], rule[1][1:]), grammar, utterance[1:], path[:], res)
            #if path and not done:
                # match((rule[0], rule[1][1:]), grammar, utterance[2:], path[:], res)
                #utterance = utterance[1:]
            return (path, done)
        elif s in left:
            new_rules = [a for a in grammar if a[0] == s]

            for new_rule in new_rules:
                # print 114, s, rule, new_rule, path
                (path, done) = match(new_rule, grammar, utterance, path + [new_rule], res)
                if path:
                    if not done:
                        utterance = utterance[1:]
                    # print 116, s, rule, new_rule, path
                    continue
                else:
                    continue
        else:
            return ([], False)
    return ([], False)

# We have provided a few test cases. You will likely want to add your own.

grammar1 = [
    ("S", ["P", ]),
    ("S", ["a", "Q", ]),
    ("P", ["a", "T"]),
    ("P", ["c"]),
    ("Q", ["b"]),
    ("T", ["b"]),
]

print isambig(grammar1, "S", ["a", "b"]) == True
print isambig(grammar1, "S", ["c"]) == False

grammar2 = [
    ("A", ["B", ]),
    ("B", ["C", ]),
    ("C", ["D", ]),
    ("D", ["E", ]),
    ("E", ["F", ]),
    ("E", ["G", ]),
    ("E", ["x", "H", ]),
    ("F", ["x", "H"]),
    ("G", ["x", "H"]),
    ("H", ["y", ]),
]
print isambig(grammar2, "A", ["x", "y"]),  True
print isambig(grammar2, "E", ["y"]), False

grammar3 = [  # Rivers in Kenya
    ("A", ["B", "C"]),
    ("A", ["D", ]),
    ("B", ["Dawa", ]),
    ("C", ["Gucha", ]),
    ("D", ["B", "Gucha"]),
    ("A", ["E", "Mbagathi"]),
    ("A", ["F", "Nairobi"]),
    ("E", ["Tsavo"]),
    ("F", ["Dawa", "Gucha"])
]
print isambig(grammar3, "A", ["Dawa", "Gucha"]), True
print isambig(grammar3, "A", ["Dawa", "Gucha", "Nairobi"]) == False
print isambig(grammar3, "A", ["Tsavo"]) == False

