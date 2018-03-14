def getsum(alist):
  if len(alist) == 1:
    return alist[0]
    
  else:
    return alist[0] + getsum(alist[1:])
    
print(getsum([2, 4, 7]))
