import math

def divisorsViaFactors(n):
    """build a dictionary to later use the equation that says adding 1 to every exponent of the list of factors and multiplying the results gives the factor count"""
    result = n
    factors = {}
    i = 2
    while result != 1:
        if result % i == 0:
            if i in factors:
                factors[i] = factors[i] + 1
            else:
                factors[i] = 1
            result = result / i
            i = 2
        else:
            i += 1
    return factors

# too slow for high divisor searches
# def countDivisors(num):
#     count = 1
#     max = int(math.ceil(num/2) + 1)
#     for i in range(1, max):
#         # print("i:" + str(i))
#         if num % i == 0:
#             count +=1
#             # print(count)
#     return count

usernum = int(input("Enter the number of divisors you want to find at least as many of for a triangle number: "))

trinum = 6
runner = 3
divcount = 1

while divcount < usernum:
    runner += 1
    trinum = trinum + runner
    divcount = 1
    triDict = divisorsViaFactors(trinum)
    for div in triDict:
        # print(div)
        # print(triDict[div])
        divcount = divcount * (triDict[div] + 1)

# print(countDivisors(usernum))
print("There are " + str(divcount) + " divisors in " + str(trinum))
