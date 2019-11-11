#! /usr/bin/python
import sys
import os
import time

 
print("Process id before forking: {}".format(os.getpid()))
 
no_of_forks = 3
if len(sys.argv) == 2:
    forks = int(sys.argv[1])
 
for i in range(no_of_forks):
    try:
        pid = os.fork()
    except OSError:
        sys.stderr.write("Could not create a child process\n")
        continue

    if pid == 0:
        print("In the child process {} that has the PID {}".format(i+1, os.getpid()))
        if i == 0:
        	print("Do this in fork-1\n")
        	'''
        	Paste your codes to do some stuff with this process
        	'''
        	print("Alexa Alexa....\n")

        if i == 1:
        	print("Do this in fork-2\n")
        	'''
        	Paste your codes to do some stuff with this process
        	'''
        	print("Okay Google....\n")

        if i == 2:
        	print("Do this in fork-3\n")
        	'''
        	Paste your codes to do some stuff with this process
        	'''
        	print("Hei Siri....\n")
        
        exit()
    else:
        print("In the parent process after forking the child {}".format(pid))
 
print("In the parent process after forking {} children".format(no_of_forks))

time.sleep(10)

for i in range(no_of_forks):
    finished = os.waitpid(0, 0)
    print(finished)