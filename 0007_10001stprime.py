index = int(input("Enter the number of the prime position you want to return: "))

def displayNthPrime(nth):
    countOfPrimes = 0
    numberToCheck = 2
    i = 2
    while countOfPrimes < index:
        currentPrimeCheck = numberToCheck
        factorCount = 0
        while currentPrimeCheck != 1:
            if currentPrimeCheck % i == 0:
                factorCount += 1
                currentPrimeCheck = currentPrimeCheck / i
                i = 2
            else:
                i += 1
        if factorCount == 1:
            countOfPrimes += 1
        numberToCheck += 1

    print("The " + str(index) + " prime is: " + str(numberToCheck - 1))

displayNthPrime(index)
