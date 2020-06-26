'''
Given an array of integers, return indices of the two numbers such 
that they add up to a specific target.
'''
def two_sum():
  numbers=[2, 8, 7, 15]
  target = 9
  for value in numbers:
    if target-value in numbers:
        return [numbers.index(value),numbers.index(target-value)]
  return "No Sum"

print(two_sum())#should print [0,2]
