import sys

class ListObject:
   """A class example that adds the elements in a list"""
   def __init__(self, newList):
      self.myList = newList
   def addList(self):
      self.mySum = 0
      for x in self.myList:
         self.mySum += int(x)


if(len(sys.argv) >= 3): 
   myListObject = ListObject(sys.argv[1:])
   myListObject.addList()
   print ("The sum is: ", myListObject.mySum)

else:
   print ("You need to include at least 2 numbers you want me to add. For example:")
   print ("python.py " + sys.argv[0], " 4 5")
   