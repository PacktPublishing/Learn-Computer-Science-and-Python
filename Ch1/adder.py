import sys

if(len(sys.argv) == 3): 
   print (sys.argv[1], " + ", sys.argv[2], " = ", int(sys.argv[1]) + int(sys.argv[2]) )
else:
   print ("You need to include the 2 numbers you want me to add. For example:")
   print ("python.py " + sys.argv[0], " 4 5")