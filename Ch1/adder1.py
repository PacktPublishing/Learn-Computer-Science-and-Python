import sys

if(len(sys.argv) == 3): 
   x = int(sys.argv[1])
   y = int(sys.argv[2])
   z = x + y
   print (x, " + ", y, " = ", z )
else:
   print ("You need to include the 2 numbers you want me to add. For example:")
   print ("python.py " + sys.argv[0], " 4 5")