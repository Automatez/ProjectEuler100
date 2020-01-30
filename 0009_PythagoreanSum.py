import math

def FindPythoTriple(targetsum):
    answer = 0
    for a in range (2, targetsum):
        for b in range (a, targetsum):
            #print(a, b)
            #print(math.sqrt(a**2 + b**2))
            #print (a + b + math.sqrt(a**2 + b**2))
            if (math.sqrt(a**2 + b**2).is_integer()) and (a + b + math.sqrt(a**2 + b**2) == targetsum):
                answer = str(a) + ' + ' + str(b) + ' + ' + str(math.sqrt(a**2 + b**2)) + ' = ' + str(targetsum) + ' and abc = ' + str(a*b*math.sqrt(a**2 + b**2))
                break
        if answer != 0:
            break
    return answer

userTarget = int(input("Enter a sum for 3 pythagorean numbers to meet: "))
print(FindPythoTriple(userTarget))

#OTHER SOLUTIONS
#I liked this one for simplifying the approach via math
# I used a little algebra for this one. Ended up in linear time, which is not too bad.
# Essentially, there is a single curve along the cone y^2 + x^2 = z^2 which also satisfies x + y + z = 1,000.
# Now, we know that only one set of whole numbers exists on that curve.
#
# First, I replaced z with (1,000 - x - y). Then I put the equation in terms of y: 100,000 = 1000y + 1000x - xy.
# Here's my code, which simply plugs in every x from 0 to 500 to see which y value also comes out whole.
#
# Hide Code
#
# def y(x):
#     return (1_000_000 - 2000 * x) / (2000 - 2 * x)
#
#
# def solve():
#     for i in range(0, 500):
#         print(f"{y(i)} {i} ")
#
#
# solve()
