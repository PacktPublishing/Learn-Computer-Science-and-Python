import sys

if(len(sys.argv) >= 3): 
   sum = 0
   for x in sys.argv[1:]:
      sum += int(x)
   print ("The sum is: ", sum)
else:
   print ("You need to include at least 2 numbers you want me to add. For example:")
   print ("python.py " + sys.argv[0], " 4 5")