def findLrgPalin(n):
    drome = []
    orig = x = y = int(str(9)*n)
    while x > 0:
        y = orig
        while y > 0:
            check = x * y
            #print('Check: ' + str(check))
            forward = str(check)
            backward = str(check)[::-1]
            #print(forward + ' and ' + backward)
            if forward == backward:
                drome.append(int(forward))
                print('drome = ' + forward)
            y -= 1
        x -= 1
    print(max(drome))

digits = int(input("How many digits do you want in the 2 nums that multiply together? "))
findLrgPalin(digits)

#OTHER SOLUTIONS
# import time
# start = time.time()
# res = []
#
# result   = lambda list: [x*y for x in range(1000) for y in range(1000) if x*y>100000]
# result_1 = lambda list: [x for x in result(res) if x%10 == x//100000 and x%100//10 == x//10000%10 and x//1000%10 == x%1000//100]
#
# answer = max(result_1(res))
#
# elapsed = (time.time() - start)
#
# print("%s found in %s seconds." % (answer,elapsed))
#
# #906609 found in 0.16495919227600098 seconds.
