#!/usr/bin/python
import sys
def fibbonaci(n):

    start = 1
    next = 1
    count = 1
    while True:
        if(count>n):
            return
        yield start
        start,next = next,start+next
        count = count+1

f =fibbonaci(10)

while True:
    try:
        print (next(f), end=" ")
    except StopIteration:
        sys.exit()



