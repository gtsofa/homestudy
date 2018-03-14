# sum of elements in a list
"""
The sum of the list alist is the sum of the first element of the list (alist[0]), 
and the sum of the numbers in the rest of the list (alist[1:])
"""

def getsum(alist):
  if len(alist) == 1:
    return alist[0]
    
  else:
    return alist[0] + getsum(alist[1:])
    
print(getsum([2, 4, 7]))
