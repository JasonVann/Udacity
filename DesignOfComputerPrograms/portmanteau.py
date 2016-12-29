# Unit 6: Fun with Words

"""
A portmanteau word is a blend of two or more words, like 'mathelete',
which comes from 'math' and 'athelete'.  You will write a function to
find the 'best' portmanteau word from a list of dictionary words.
Because 'portmanteau' is so easy to misspell, we will call our
function 'natalie' instead:

    natalie(['word', ...]) == 'portmanteauword' 

In this exercise the rules are: a portmanteau must be composed of
three non-empty pieces, start+mid+end, where both start+mid and
mid+end are among the list of words passed in.  For example,
'adolescented' comes from 'adolescent' and 'scented', with
start+mid+end='adole'+'scent'+'ed'. A portmanteau must be composed
of two different words (not the same word twice).

That defines an allowable combination, but which is best? Intuitively,
a longer word is better, and a word is well-balanced if the mid is
about half the total length while start and end are about 1/4 each.
To make that specific, the score for a word w is the number of letters
in w minus the difference between the actual and ideal lengths of
start, mid, and end. (For the example word w='adole'+'scent'+'ed', the
start,mid,end lengths are 5,5,2 and the total length is 12.  The ideal
start,mid,end lengths are 12/4,12/2,12/4 = 3,6,3. So the final score
is

    12 - abs(5-3) - abs(5-6) - abs(2-3) = 8.

yielding a score of 12 - abs(5-(12/4)) - abs(5-(12/2)) -
abs(2-(12/4)) = 8.

The output of natalie(words) should be the best portmanteau, or None
if there is none. 

Note (1): I got the idea for this question from
Darius Bacon.  Note (2): In real life, many portmanteaux omit letters,
for example 'smoke' + 'fog' = 'smog'; we aren't considering those.
Note (3): The word 'portmanteau' is itself a portmanteau; it comes
from the French "porter" (to carry) + "manteau" (cloak), and in
English meant "suitcase" in 1871 when Lewis Carroll used it in
'Through the Looking Glass' to mean two words packed into one. Note
(4): the rules for 'best' are certainly subjective, and certainly
should depend on more things than just letter length.  In addition to
programming the solution described here, you are welcome to explore
your own definition of best, and use your own word lists to come up
with interesting new results.  Post your best ones in the discussion
forum. Note (5) The test examples will involve no more than a dozen or so
input words. But you could implement a method that is efficient with a
larger list of words.
"""

def cal_score(state):
    (start, mid, end) = state
    n = sum(len(x) for x in state)
    score = n - abs(n/4.0- len(start)) - abs(len(mid) - n/2.) - abs(n/4. - len(end))
    return score
    
state = ('adole', 'scent', 'ed')
state = ('armaged', 'don', 'ald') # 6
#state = ('ph', 'arma', 'geddon') # 6
print 61, cal_score(state)

import itertools

def break_words(a, b):
    if b in a or a in b:
        return None
    n = len(a)
    res = None
    for j in range(1, n, 1):
        if a[n - j:] == b[:j]:
            res = j
            j += 1
    if res == None:
        return
    state = (a[:n-res], a[n-res:], b[res:])
    return state
    
#print 79, break_words('adolescent', 'scented')
print 79, break_words('pharma', 'armageddon')

state = ('armageddon', 'pharma', 'geddon') # 11

def natalie(words):
    "Find the best Portmanteau word formed from any two of the list of words."
    cands = itertools.permutations(words, 2)
    best = 0
    res = None
    for (a, b) in cands:
        if a == b:
            continue
        #print 71, a, b
        state = break_words(a, b)
        if state is None:
            continue
        score = cal_score(state)
        if score > best:
            best = score
            res = state
    #print 97, res
    return None if res is None else ''.join(list(res))
    
def test_natalie():
    "Some test cases for natalie"
    assert natalie(['adolescent', 'scented', 'centennial', 'always', 'ado']) in ('adolescented','adolescentennial')
    assert natalie(['eskimo', 'escort', 'kimchee', 'kimono', 'cheese']) == 'eskimono'
    assert natalie(['kimono', 'kimchee', 'cheese', 'serious', 'us', 'usage']) == 'kimcheese'
    assert natalie(['circus', 'elephant', 'lion', 'opera', 'phantom']) == 'elephantom'
    assert natalie(['programmer', 'coder', 'partying', 'merrymaking']) == 'programmerrymaking'
    assert natalie(['int', 'intimate', 'hinter', 'hint', 'winter']) == 'hintimate'
    assert natalie(['morass', 'moral', 'assassination']) == 'morassassination'
    assert natalie(['entrepreneur', 'academic', 'doctor', 'neuropsychologist', 'neurotoxin', 'scientist', 'gist']) in ('entrepreneuropsychologist', 'entrepreneurotoxin')
    assert natalie(['perspicacity', 'cityslicker', 'capability', 'capable']) == 'perspicacityslicker'
    assert natalie(['backfire', 'fireproof', 'backflow', 'flowchart', 'background', 'groundhog']) == 'backgroundhog'
    assert natalie(['streaker', 'nudist', 'hippie', 'protestor', 'disturbance', 'cops']) == 'nudisturbance'
    assert natalie(['night', 'day']) == None
    assert natalie(['dog', 'dogs']) == None
    assert natalie(['test']) == None
    assert natalie(['']) ==  None
    assert natalie(['ABC', '123']) == None
    assert natalie([]) == None
    return 'tests pass'

def test_natalie():
    "Some test cases for natalie"
    assert (natalie(['armageddon', 'pharma', 'karma', 'donald', 'donut'])
            == 'pharmageddon')
            
    assert (natalie(['eskimo', 'escort', 'kimchee', 'kimono', 'cheese'])
            == 'eskimono')
    assert (natalie(['kimono', 'kimchee', 'cheese', 'serious', 'us', 'usage'])
            == 'kimcheese')
    assert (natalie(['circus', 'elephant', 'lion', 'opera', 'phantom'])
            == 'elephantom')
    assert (natalie(['adolescent', 'scented', 'centennial', 'always',
                    'ado', 'centipede'])
            in ( 'adolescented', 'adolescentennial', 'adolescentipede'))
    assert (natalie(['programmer', 'coder', 'partying', 'merrymaking'])
            == 'programmerrymaking')
    assert (natalie(['int', 'intimate', 'hinter', 'hint', 'winter'])
            == 'hintimate')
    assert (natalie(['morass', 'moral', 'assassination'])
            == 'morassassination')
    assert (natalie(['entrepreneur', 'academic', 'doctor',
                     'neuropsychologist', 'neurotoxin', 'scientist', 'gist'])
            in ('entrepreneuropsychologist', 'entrepreneurotoxin'))
    assert (natalie(['perspicacity', 'cityslicker', 'capability', 'capable'])
            == 'perspicacityslicker')
    assert (natalie(['backfire', 'fireproof', 'backflow', 'flowchart',
                     'background', 'groundhog'])
            == 'backgroundhog')
    assert (natalie(['streaker', 'nudist', 'hippie', 'protestor',
                     'disturbance', 'cops'])
            == 'nudisturbance')
    assert (natalie(['night', 'day']) == None)
    assert (natalie(['dog', 'dogs']) == None)
    assert (natalie(['test']) == None)
    assert (natalie(['']) ==  None)
    assert (natalie(['ABC', '123']) == None)
    assert (natalie([]) == None)
    assert (natalie(['pedestrian', 'pedigree', 'green', 'greenery'])
            == 'pedigreenery')
    
    
    
    assert (natalie(['lagniappe', 'appendectomy', 'append', 'lapin'])
            == 'lagniappendectomy')
    assert (natalie(['angler', 'fisherman', 'boomerang', 'frisbee', 'rangler',
                     'ranger', 'rangefinder'])
            in ('boomerangler', 'boomerangefinder'))
    assert (natalie(['freud', 'raelian', 'dianetics', 'jonestown', 'moonies'])
            == 'freudianetics')
    assert (natalie(['atheist', 'math', 'athlete', 'psychopath'])
            in ('psychopatheist', 'psychopathlete'))
    assert (natalie(['hippo', 'hippodrome', 'potato', 'dromedary'])
            == 'hippodromedary')
    
    assert (natalie(['taxi', 'taxicab', 'cabinet', 'cabin',
                     'cabriolet', 'axe'])
            in ('taxicabinet', 'taxicabriolet'))
    
    assert (natalie(['pocketbook', 'bookmark', 'bookkeeper', 'goalkeeper'])
            in ('pocketbookmark', 'pocketbookkeeper'))
    assert (natalie(['athlete', 'psychopath', 'athletic', 'axmurderer'])
            in ('psychopathlete', 'psychopathletic'))
    assert (natalie(['info', 'foibles', 'follicles'])
            == 'infoibles')
    assert (natalie(['moribund', 'bundlers', 'bundt'])
            == 'moribundlers')

import time

start = time.time()
print test_natalie(), time.time() - start



