import sys

def addList(listToAdd):
   sum = 0
   for x in listToAdd:
      sum += int(x)
   return sum

if(len(sys.argv) >= 3): 
   print ("The sum is: ", addList(sys.argv[1:]))
   print ("The sum without the first element is: ", addList(sys.argv[2:]))

else:
   print ("You need to include at least 2 numbers you want me to add. For example:")
   print ("python.py " + sys.argv[0], " 4 5")
   
   