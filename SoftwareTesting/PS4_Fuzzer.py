# Fuzz Testing
# ------------
# Write a random fuzzer, based on Charlie Miller's example
# from Problem Set 4, for a text viewer application.
#
# For multiple iterations, the procedure, fuzzit, should take in the content
# of a text file, pass the content into a byte array, randomly modify bytes
# of the "file", and add the resulting byte array (as a String) to a list. 
# The return value of the fuzzit procedure should be a list of 
# byte-modified strings.


import random
import math
import string
import subprocess
import time

file_list = ['C4M1L4_Lec1_Introduction.pptx.pdf']
app_list = ['/Applications/Preview.app/Contents/MacOS/Preview']

content = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Phasellus sollicitudin condimentum libero,
sit amet ultrices lacus faucibus nec.
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Cum sociis natoque penatibus et magnis dis parturient montes,
nascetur ridiculus mus. Cras nulla nisi, accumsan gravida commodo et,
venenatis dignissim quam. Mauris rutrum ullamcorper consectetur.
Nunc luctus dui eu libero fringilla tempor. Integer vitae libero purus.
Fusce est dui, suscipit mollis pellentesque vel, cursus sed sapien.
Duis quam nibh, dictum ut dictum eget, ultrices in tortor.
In hac habitasse platea dictumst. Morbi et leo enim.
Aenean ipsum ipsum, laoreet vel cursus a, tincidunt ultrices augue.
Aliquam ac erat eget nunc lacinia imperdiet vel id nulla."""

fuzz_output = '/Users/jasonniu/Documents/Projects/MOOC/Udacity/SoftwareTesting/fuzz.pdf'
FuzzFactor = 25

def fuzzit(content):
# Write a random fuzzer for a simulated text viewer application
    
    num_tests = 1
    A = []
    fail = 0
    for i in range(num_tests):
        file = random.choice(file_list)
        app = random.choice(app_list)
        buf = bytearray(open(file, 'rb').read())
        # Charlie Miller's Method
        num = random.randrange(math.ceil((float(len(buf)) / FuzzFactor))) + 1
        for j in range(num):
            rbyte = random.randrange(256)
            rn = random.randrange(len(buf))
            buf[rn] = "%c"%(rbyte)
        A.append(str(buf))
        open(fuzz_output, 'wb').write(buf)
        process = subprocess.Popen([app, fuzz_output])

        time.sleep(1)
        crashed = process.poll()
        if not crashed:
            process.terminate()
        else:
            fail += 1
    print fail
    #return A
    
fuzzit(content)
