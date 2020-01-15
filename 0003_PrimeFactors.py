def findFactors(n):
    result = n
    factors = []
    i = 2
    while result != 1:
        if result % i == 0:
            factors.append(i)
            result = result / i
            i = 2
        else:
            i += 1
    return factors
    # for f in factors:
    #     if len(findFactors(f)) == 1:
    #         print(f)

n = int(input("Enter a number to find all factors:  "))
facts = findFactors(n)

for f in facts:
    if len(findFactors(f)) ==1:
        print(f)

#OTHER SOLUTIONS
#The only other interesting update I found was this to get the one number you need:
#print(max(list))
