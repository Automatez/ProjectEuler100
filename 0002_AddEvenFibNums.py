def fibEvenTotal(n):
    """where n is the Fib number to not exceed"""
    prevFib = 1
    currentFib = 2
    tempPrevious = 0
    runningTotal = 0


    while currentFib < n:
        if currentFib%2 == 0:
            runningTotal += currentFib
        tempPrevious = currentFib
        currentFib += prevFib
        prevFib = tempPrevious

    print(runningTotal)

maxFibNum = int(input("Enter the max Fibonacci number thru which to sum even Fib numbers: "))
fibEvenTotal(maxFibNum)


#SHORTER SOLUTION
Python 3 Code

def fib(num):
    sum, a, b = 0, 1, 2
    for i in range(num):
        while a < 4000000:
            print(a)
            if a % 2 == 0:
                sum += a
            a, b = b, a + b
    print(sum)
#fib(100)
