'''  Google Former Interview Question:
   Given a string S and a set of words D, 
   find the longest word in D that is a 
   subsequence of S.
   For example, given the input of 
   S = "abppplee" and 
   D = {"able", "ale", "apple", "bale", "kangaroo"}
   the correct output would be "apple"'''

def check(match,word):
  count=0
  for letter in word:
    #counts the occurrence of letters in the word to be matched
    if letter in match:
      count+=1
  return count#returns the count of letters

def extract():
  s='abbppplee'
  d={"able", "ale", "apple", "bale", "kangaroo"}
  length=0
  wrd=''
  for value in d:
    #passing individual values of dictionary along with word to be matched
    res=check(s,value)
    if res>length:#if count is greater than the length of previous words
      wrd=value#storing the word
      length=res#storing the length of the word
  print('The subsequence of ',s,'is:',wrd)#the subsequence is printed

extract()
