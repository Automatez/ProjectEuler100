import math

# this was way too slow
def determinePrimeness(count):
    i = 2
    factorCount = 0
    currentPrimeCheck = count
    primeList = [2, 3, 5, 7, 11, 13, 17, 19, 23, 27, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97] #, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
    highestPossDivisor = math.sqrt(count)
    while i <= highestPossDivisor: # and factorCount < 2
        # print('factorcount: ' + str(factorCount))
        # print('i: ' + str(i))
        # print('currentPrimeCheck: ' + str(currentPrimeCheck))

        # check against the prime list first to speed up the search
        # if currentPrimeCheck > 199:
        #     for prime in primeList:
        #         if currentPrimeCheck % prime == 0:
        #             factorCount += 1
        #             currentPrimeCheck = currentPrimeCheck / i

        # this for loop of checking against first 100 primes seems too slow
        # for j in primeList:
        #     # print(j)
        #     if currentPrimeCheck % j == 0:
        #         factorCount = 1
        #         i = count
        #         break

        if factorCount == 0 and currentPrimeCheck % i == 0:
            factorCount += 1
            i = 2
        elif factorCount == 0:
            if i == 2:
                i += 1
            else:
                i += 2
        elif factorCount > 0:
            break
            # print('new i: ' + str(i))
        # if currentPrimeCheck % 3 == 0 or currentPrimeCheck % 5 == 0 or currentPrimeCheck % 7 == 0:
        #     currentPrimeCheck = 1
    if factorCount == 0:
        # print('true')
        return(count)
    else:
        return(0)

def SumPrimes(n):
    """sum all primes below the number n"""
    #start with count 34 to check only primes over 200 since under is done
    count = 1
    #start with all primes under 200 summed up (4254) as they are not checked
    sumOfPrimes = 5
    # all primes over 5 meet the equation 6x +- 1
    while (6*count + 1) < n:
        sumOfPrimes += determinePrimeness(6*count+1)
        sumOfPrimes += determinePrimeness(6*count-1)
        # plus = determinePrimeness(6*count+1)
        # minus = determinePrimeness(6*count-1)
        # if plus > 0:
        #     sumOfPrimes += plus
        #     # print(plus)
        # elif minus > 0:
        #     sumOfPrimes += minus
            # print(minus)
            # print('new sum of primes is: ' + str(sumOfPrimes))
        count += 1
    print(sumOfPrimes)

# numb = int(input("Enter a number to see if it's prime: "))
# determinePrimeness(numb)
#
sumUnder = int(input("Enter a number (more than 200) under which to sum all primes: "))
SumPrimes(sumUnder)
