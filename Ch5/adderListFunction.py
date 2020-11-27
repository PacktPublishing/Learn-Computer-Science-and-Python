import sys
import functools

def adder(x,y): return (x+y)

if(len(sys.argv) >= 3): 
   inputs = list(map(int, sys.argv[1:]))
   print ("Sum = ", functools.reduce(adder, inputs) )
else:
   print ("You need to include at least 2 numbers you want me to add. For example:")
   print ("python.py " + sys.argv[0], " 4 5 6")