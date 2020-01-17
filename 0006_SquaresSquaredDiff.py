n = int(input("Enter number of natural numbers to compute squares/squared sum difference: "))
sumOfSquares = ((2*n+1)*n*(n+1))/6
squareOfSum = (sum(x for x in range(1,n+1)))**2
print('SoSq - SqoS: ' + str(squareOfSum) + '-' + str(sumOfSquares) + '=' + str(squareOfSum-sumOfSquares))

#OTHER SOLUTIONS
#This was the simplest of the looping solutions that I found
# sumSquare=0
# squareSum=0
# for i in range(1,101):
#     sumSquare+=i**2
#     squareSum+=i
# print(squareSum**2-sumSquare)
