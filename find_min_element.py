# find the minimum element in a list

"""
example: alist = [5,4,2,1,0]
steps:
-minelement == first element in a list when sorted( ascending order)
-result = alist[0] ie store the first index element in a result
-loop/iterate through the list and check if the first element is the min/smallest
-loop/iterate again through the list and compare that value to the next 2nd element in the list
-if i > j : then i[that value] is not the smallest
-return either true/false for the 2nd loop
-done with the two loops 
-return the result
-
-if true return the overallmin element
"""
def findMin(alist):
  result = alist[0]
  for i in alist:
    isitsmall = True 
    for j in alist:
      if i > j:
        isitsmall = False
    if isitsmall:
      result = i 
  return result
  #print(result)
  
print(findMin([5,4,2,1,0]))
