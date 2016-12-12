# CORRECT SPECIFICATION:
#
# the Queue class provides a fixed-size FIFO queue of integers
#
# the constructor takes a single parameter: an integer > 0 that
# is the maximum number of elements the queue can hold.
#
# empty() returns True if and only if the queue currently 
# holds no elements, and False otherwise.
#
# full() returns True if and only if the queue cannot hold 
# any more elements, and False otherwise.
#
# enqueue(i) attempts to put the integer i into the queue; it returns
# True if successful and False if the queue is full.
#
# dequeue() removes an integer from the queue and returns it,
# or else returns None if the queue is empty.
#
# Example:
# q = Queue(1)
# is_empty = q.empty()
# succeeded = q.enqueue(10)
# is_full = q.full()
# value = q.dequeue()
#
# 1. Should create a Queue q that can only hold 1 element
# 2. Should then check whether q is empty, which should return True
# 3. Should attempt to put 10 into the queue, and return True
# 4. Should check whether q is now full, which should return True
# 5. Should attempt to dequeue and put the result into value, which 
#    should be 10
#
# Your test function should run assertion checks and throw an 
# AssertionError for each of the 5 incorrect Queues. Pressing 
# submit will tell you how many you successfully catch so far.


from queue_test import *

def test():
    ###Your code here.
    q = Queue(0)
    assert q.empty() == True
    assert q.full() == True
    assert q.enque(1) == False
    assert q.deque() == None
    
    q = Queue(2)
    is_empty = q.empty()
    assert is_empty == True
    value = q.dequeue()
    assert value == None
    is_full = q.full()
    assert is_full == False
    
    # Insert 1st item
    succeeded = q.enqueue(10)
    assert succeeded == True
    is_full = q.full()
    assert is_full == False
    is_empty = q.empty()
    assert is_empty == False

    value = q.dequeue()
    assert value != None
    #assert value == item2
    is_empty = q.empty()
    assert is_empty == True
    is_full = q.full()
    assert is_full == False

    succeeded = q.enqueue(10)

    # Insert 2nd item
    value = q.enqueue(11)
    assert value == True
    is_empty = q.empty()
    assert is_empty == False
    is_full = q.full()
    assert is_full == True
    
    # Cannot insert any more
    value = q.enqueue(12)
    assert value == False
    is_full = q.full()
    assert is_full == True
    is_empty = q.empty()
    assert is_empty == False

    # Deque
    value = q.dequeue()
    assert value != None
    #assert value == item2
    is_empty = q.empty()
    assert is_empty == False
    is_full = q.full()
    assert is_full == False

    # Enque again
    value = q.enqueue(13)
    assert value == True
    is_full = q.full()
    assert is_full == True
    is_empty = q.empty()
    assert is_empty == False

    value = q.dequeue()
    assert value != None
    is_empty = q.empty()
    assert is_empty == False
    is_full = q.full()
    assert is_full == False
    
    # Deque last item
    value = q.dequeue()
    assert value != None
    is_empty = q.empty()
    assert is_empty == True
    is_full = q.full()
    assert is_full == False

    value = q.dequeue()
    assert value == None

    is_full = q.full()
    assert is_full == False
    is_empty = q.empty()
    assert is_empty == True



