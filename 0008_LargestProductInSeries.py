digitsToMultiply = int(input("Enter how many digits to find the largest product of: "))
#sequence = '123456'
sequence = '7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'
setToCheck = sequence[:digitsToMultiply]

highestProduct = 0
for x in range(digitsToMultiply, len(sequence)+1):
    #print('settocheck: ' + str(setToCheck))
    #print('x: ' + str(x))
    currentHighestProduct = 1
    for num in setToCheck:
        #print('num: ' + str(num))
        currentHighestProduct = int(num)*currentHighestProduct
        #print('Curr High Prod: ' + str(currentHighestProduct))
    if currentHighestProduct > highestProduct:
        #print('highestProduct: ' + str(highestProduct))
        highestProduct = currentHighestProduct
    #print(x)
    #print(int(x))
    if int(x) < len(sequence):
        setToCheck = setToCheck[1:] + sequence[x]
    #print('SetToCheck: ' + str(setToCheck))

print('The largest product in this sequence of ' + str(digitsToMultiply) + ' consecutive digits is: ' + str(highestProduct))

#OTHER SOLUTIONS
#This one had good features I had not used
:
# import numpy as np
#
# digitnum = str(7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450)
# digitlist = []
# biggestnum = 0
#
# #convert str to a list of 1 digit numbers
# for i in digitnum:
#     digitlist.append(int(i))
#
# #iterate over a 13 digit wide range advancing one digit at a time
# for ind, value in enumerate(digitlist):
#     if np.prod(np.array(digitlist[ind:ind+13])) > biggestnum:
#         biggestnum = np.prod(np.array(digitlist[ind:ind+13]))
#     else:
#         continue
#
# print(f"Biggest number is {biggestnum}")