"""
Sample Space Generator
Used to determine and print a sample space set given parameters
Will presume values are desired as elements instead of strings
"""

# for establishing the maximum number of possible elements, 
# input of an expression is required to determine maximum
# associate the maximum possible number of elements with keyword maxElem
print('Enter the mathematical expression for maximum number of outcomes here:')
maxElem = int(eval(input()))
print('Statement for max outcomes evaluates to', str(maxElem) + '.')

# print sample space chronologically sequenced minimum to maximum # outcomes
# For guide on for loop for this algorithm, refer to: 
# https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
sampleSpace = []
for x in range(maxElem):
    sampleSpace.append(x+1)
print('Sample Space: \n', sampleSpace)
