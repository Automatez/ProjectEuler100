thruNumber = int(input("Please enter the number thru which you want to add all multiples of 3 and 5: "))

#incorrectlty listed every item in first iteration
# multiplesList = []
# for num in range(thruNumber):
#     if num%3 == 0 or num%5 == 0:
#         multiplesList.append(num)
#
# for num in multiplesList:
#     print(num, end = ' ')

#MYSOLUTION
sum = 0
for num in range(thruNumber):
    if num%3 == 0 or num%5 == 0:
        sum += num

print(sum)

#OTHERSOLUTIONS
#super short solution online:
#len("sum([x for x in range(1000) if not x%3 or not x%5])")
