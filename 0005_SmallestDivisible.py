
def findFactors(n):
    """builds a list of all factors for a number"""
    result = n
    factors = {}
    i = 2
    while result != 1:
        if result % i == 0:
            if i in factors: #CORRECT THIS
                factors[i] = factors[i] + 1
            else:
                factors[i] = 1
            result = result / i
            i = 2
        else:
            i += 1
    return factors

def lowestCommonMultiple(dictOfPowers):
    """takes a dictionary with key:value of number:power and calcs with the power then multiplies the results"""
    calculatedFactor = 1
    for factor in dictOfPowers:
        calculatedFactor = calculatedFactor * (factor**dictOfPowers[factor])
    return calculatedFactor


numForLCM = int(input("Enter a number to find the lowest common multiple of it and all preceding: "))
# loops through all numbers building indiv dicts and comparing them as it goes to builds a single dict that has just the largest power of each factor that uniquely appears across all numbers
factorPowerDict = {}
for nums in range(1, numForLCM):
    currentDict = findFactors(nums)
    for factor in currentDict:
        if factor in factorPowerDict:
            if currentDict[factor] > factorPowerDict[factor]:
                factorPowerDict[factor] = currentDict[factor]
        else:
            factorPowerDict[factor] = currentDict[factor]

print('The largest factor:power pairs that have to be multiplied out to get the LCM are:')
for keyz in factorPowerDict:
    print(str(keyz) + ':' + str(factorPowerDict[keyz]))
print(lowestCommonMultiple(factorPowerDict))

#OTHER SOLUTIONS
#solutions were mostly brute force - finally found one similar to mine that ran fast
# 
# import math
# input = 20
#
# # find prime numbers smaller or equall to input
# lst_prime = [2]
# for num in range(3,input,2):
# 	if all(num%i!=0 for i in range(3,int(math.sqrt(num))+1, 2)):
# 		lst_prime.append(num)
#
# print(lst_prime)
#
# # find the highest power for each prime numbers
# result = 1
# for item in range(len(lst_prime)):
# 	power = 1
# 	while pow(lst_prime[item], power) <= input:
# 		power += 1
# 	result *= pow(lst_prime[item], power-1)
#
# print(result)


#brute force did not seem to work for large numbers
# def findFirstDivisible(n):
#     """find the lowest number evenly divisible by every number from 1 to n """
#     rem = 0
#     answer = 0
#     numsToCheck = n
#     #while numsToCheck < 15:
#     while answer == 0:
#         for i in range(1, numsToCheck):
#             #print(i)
#             if numsToCheck % i != 0:
#                 break
#             elif i == n:
#                 answer = numsToCheck
#                 #print('Answer: ' + str(answer))
#         numsToCheck += 1
#         #print('numstoCheck: ' + str(numsToCheck))
#
#     print(str(answer))
#
# numChosen = int(input("Enter the top end of a range you want to find a lowest common multiple for: "))
# findFirstDivisible(numChosen)
