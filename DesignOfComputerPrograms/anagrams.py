# -----------------
# User Instructions
# 
# This homework deals with anagrams. An anagram is a rearrangement 
# of the letters in a word to form one or more new words. 
#
# Your job is to write a function anagrams(), which takes as input 
# a phrase and an optional argument, shortest, which is an integer 
# that specifies the shortest acceptable word. Your function should
# return a set of all the possible combinations of anagrams. 
#
# Your function should not return every permutation of a multi word
# anagram: only the permutation where the words are in alphabetical
# order. For example, for the input string 'ANAGRAMS' the set that 
# your function returns should include 'AN ARM SAG', but should NOT 
# include 'ARM SAG AN', or 'SAG AN ARM', etc...

# 'TORCHWOOD'

def anagrams(phrase, shortest=2):
    """Return a set of phrases with words from WORDS that form anagram
    of phrase. Spaces can be anywhere in phrase or anagram. All words 
    have length >= shortest. Phrases in answer must have words in 
    lexicographic order (not all permutations)."""
    # your code here
    phrase = phrase.split()
    phrase = ''.join(phrase)
    words = find_words(phrase)
    words = [p for p in words if len(p) >= shortest]
    #letters = set(phrase)
    #print 26, words, phrase
    results = set()
    build(words, phrase, results, [])
    #print 38, results
    return results
    
def build(words, phrase, results, cur):
    if phrase == '' or len(words) == 0:
        #print 42, cur
        cur.sort()
        cur = ' '.join(cur)
        #print 44, cur
        results.add(cur)
        #print 45, results
        return results
    
    for word in words:
        if not is_valid(word, phrase):
            continue
        left = removed(phrase, word)
        '''
        if word == 'DOCTOR':
            print 48, word, phrase, left
        '''
        words1 = words[:]
        words1.remove(word)
        cur1 = cur[:]
        cur1 += [word]
        build(words1, left, results, cur1)
    
def is_valid(word, phrase):
    p = list(phrase)
    for w in word:
        if w in p:
            p.remove(w)
        else:
            return False
    return True
    
#print 63, is_valid('DO', 'TORCHO')
    
# ------------
# Helpful functions
# 
# You may find the following functions useful. These functions
# are identical to those we defined in lecture. 

def removed(letters, remove):
    "Return a str of letters, but with each letter in remove removed once."
    for L in remove:
        letters = letters.replace(L, '', 1)
    return letters

def find_words(letters):
    return extend_prefix('', letters, set())

def extend_prefix(pre, letters, results):
    if pre in WORDS: results.add(pre)
    if pre in PREFIXES:
        for L in letters:
            extend_prefix(pre+L, letters.replace(L, '', 1), results)
    return results

def prefixes(word):
    "A list of the initial sequences of a word, not including the complete word."
    return [word[:i] for i in range(len(word))]

def readwordlist(filename):
    "Return a pair of sets: all the words in a file, and all the prefixes. (Uppercased.)"
    wordset = set(open(filename).read().upper().split())
    prefixset = set(p for word in wordset for p in prefixes(word))
    return wordset, prefixset

WORDS, PREFIXES = readwordlist('words4k.txt')

#print anagrams('TORCHWOOD')
#print 112, anagrams('OCTOBER SKY')

# ------------
# Testing
# 
# Run the function test() to see if your function behaves as expected.

def test():
    assert 'DOCTOR WHO' in anagrams('TORCHWOOD')
    assert 'BOOK SEC TRY' in anagrams('OCTOBER SKY')
    assert 'SEE THEY' in anagrams('THE EYES')
    assert 'LIVES' in anagrams('ELVIS')
    assert anagrams('PYTHONIC') == set([
        'NTH PIC YO', 'NTH OY PIC', 'ON PIC THY', 'NO PIC THY', 'COY IN PHT',
        'ICY NO PHT', 'ICY ON PHT', 'ICY NTH OP', 'COP IN THY', 'HYP ON TIC',
        'CON PI THY', 'HYP NO TIC', 'COY NTH PI', 'CON HYP IT', 'COT HYP IN',
        'CON HYP TI'])
    return 'tests pass'

import time
start = time.time()
print test(), time.time() - start


