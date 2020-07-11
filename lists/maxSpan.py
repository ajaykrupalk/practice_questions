'''Consider the leftmost and righmost appearances of some value in an array. We'll say that the "span" is the number of elements between the two inclusive. A single value has a span of 1. Returns the largest span found in the given array. (Efficiency is not a priority.)
'''
def maxSpan(array):
  pos={}#dictionary to store indices of occurrances of numbers
  for index,element in enumerate(array):
    if element not in pos:
      pos[element]=[]#storing the positions as lists e.g. {1:[0,3],4:[1,4,5,6],2:[2]}
    pos[element].append(index)#adding the indices to the lists
  maxspan=1
  for ele in pos:
    span=pos[ele][-1]-pos[ele][0]+1#getting the span of elements
    if span>maxspan:#getting the largest span
      maxspan=span
  return maxspan

print('The max span is:',maxSpan([1, 4, 2, 1, 4, 4, 4])) 
