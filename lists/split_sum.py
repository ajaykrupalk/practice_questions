'''Given a non-empty array, return true if there is a place to split the array so that the sum of the numbers on one side is equal to the sum of the numbers on the other side.'''
def find(array):
  mid=(len(array)-1)//2
  a=sum(array[:mid+1])#getting the first half
  b=sum(array[mid+1:])#getting the second half
  print(a==b)

find([1,1,1,2,1])
