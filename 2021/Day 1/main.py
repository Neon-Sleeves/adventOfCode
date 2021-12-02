from nums import numbers as numList
from nums import convertSliding
# GOALS:
# convert sliding into list of sum of each set
# use countIncrease on that
slidingNumbers = []

convertSliding(numList, slidingNumbers)

def sumOfSets(inList):
  result = []
  for numSet in inList:
    result.append(sum(numSet))
  return result

def getInDe(inList): 
  result = []
  index = 0
  for number in inList[1:len(inList)]:
    index += 1
    if number > inList[index - 1]:
      result.append(1)
    else:
      result.append(0)
  return result

def checkDupes(inList):
  for number in inList:
    if inList.count(number) != 1:
      print(number)

def countIncrease(inList):
  return getInDe(inList).count(1)

print(countIncrease(sumOfSets(slidingNumbers)))
