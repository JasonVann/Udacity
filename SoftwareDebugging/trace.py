#!/usr/bin/env python
# Simple debugger
# See instructions around line 85
import sys
import readline

# Our buggy program
def remove_html_markup(s):
    tag   = False
    quote = False
    out   = ""

    for c in s:
        if c == '<' and not quote:
            tag = True
        elif c == '>' and not quote:
            tag = False
        elif c == '"' or c == "'" and tag:
            quote = not quote
        elif not tag:
            out = out + c
    return out
    
# main program that runs the buggy program
def main():
    print remove_html_markup('"<b>foo</b>"')

# globals
breakpoints = {}
watchpoints = {"quote": True}
watch_values = {}
stepping = True

"""
Our debug function
"""
def debug(command, my_locals):
    global stepping
    global breakpoints
    #print 40, my_locals
    if command.find(' ') > 0:
        arg = command.split(' ')[1]
    else:
        arg = None

    if command.startswith('s'):     # step
        stepping = True
        return True
    elif command.startswith('c'):   # continue
        stepping = False
        return True
    elif command.startswith('p'):    # print 
        # FIRST ASSIGNMENT CODE
        if arg == None:
            print my_locals
        else:
            if arg in my_locals:
                print arg, '=', repr(my_locals[arg])
            else:
                print 'No such variable:', arg
    elif command.startswith('b'):    # breakpoint         
        # SECOND ASSIGNMENT CODE
        if arg == None:
            print 'You must supply a line number'
        else:
            breakpoints[int(arg)] = True
    elif command.startswith('w'):    # watch variable
        # YOUR CODE HERE
        if arg == None:
            print 'You must supply a variable name'
        else:
            watchpoints[arg] = True
    elif command.startswith('q'):   # quit
        print "Exiting my-spyder..."
        sys.exit(0)
    else:
        print "No such command", repr(command)
        
    return False

commands = ["w c", "c", "c", "w out", "c", "c", "c", "q"]

def input_command():
    #command = raw_input("(my-spyder) ")
    global commands
    command = commands.pop(0)
    return command

"""
Our traceit function
Improve the traceit function to watch for variables in the watchpoint 
dictionary and print out (literally like that): 
event, frame.f_lineno, frame.f_code.co_name
and then the values of the variables, each in new line, in a format:
somevar ":", "Initialized"), "=>", repr(somevalue)
if the value was not set, and got set in the line, or
somevar ":", repr(old-value), "=>", repr(new-value)
when the value of the variable has changed.
If the value is unchanged, do not print anything.
"""
f_locals0 = {}
def traceit(frame, event, trace_arg):
    global stepping
    import copy
    global f_locals0
    #f_locals0 = {}
    if event == 'line':
        if stepping or breakpoints.has_key(frame.f_lineno):
            resume = False
            while not resume:
                print event, frame.f_lineno, frame.f_code.co_name, frame.f_locals
                command = input_command()
                resume = debug(command, frame.f_locals)
                
    #print 111, frame.f_locals, f_locals0
    #print 112, watchpoints, frame.f_lineno, len(frame.f_locals), len(watchpoints)
    #command = input_command()
        
        #print 118, command, frame.f_lineno
            
        #if len(frame.f_locals) > 0 and len(watchpoints) > 0:
        if True:
            #debug(command, frame.f_locals)
            for var in watchpoints:
                #print 121, var, var in f_locals0, var in frame.f_locals
                if var not in frame.f_locals:
                    continue
                if var not in f_locals0 or f_locals0[var] == None:
                    #if frame.f_locals[var] != None:
                    print 'line', frame.f_lineno, frame.f_code.co_name
                    print var, ":", "Initialized =>", repr(frame.f_locals[var])
                elif var in f_locals0 and var in frame.f_locals:
                    new_v = frame.f_locals[var] 
                    old_v = f_locals0[var]
                    if new_v != old_v:
                        print 'line', frame.f_lineno, frame.f_code.co_name
                        print var, ":", repr(old_v), "=>", repr(new_v)
        
        f_locals0 = copy.deepcopy(frame.f_locals)
        #print 130, frame.f_locals, f_locals0
    return traceit


# Using the tracer
sys.settrace(traceit)
main()
sys.settrace(None)


# with the commands = ["w c", "c", "c", "w out", "c", "c", "c", "q"],
# the output should look like this (line numbers may be different):
#line 26 main {}
#line 10 remove_html_markup
#quote : Initialized => False
#line 13 remove_html_markup
#c : Initialized => '"'
#line 19 remove_html_markup
#quote : False => True
#line 13 remove_html_markup
#c : '"' => '<'
#line 21 remove_html_markup
#out : '' => '<'
#Exiting my-spyder...
