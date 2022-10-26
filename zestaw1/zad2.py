import math
from collections import defaultdict
import sys 

argv = sys.argv[1:]
numbers = [int(x) for x in argv]
for number in numbers:
    print(number, "=", end=" ")
    sqr = int(math.sqrt(number))
    k = 2
    num = defaultdict(int)
    while number > 1 & k < sqr:
        while number % k == 0:
            num[str(k)] += 1
            number /= k
        k+=1
    for i, element in enumerate(num):
        if num[element] > 1:
            print(str(element), "^", num[element], end="", sep="")
        else:
            print(str(element), end="")
        if i != len(num) - 1:
            print("*", end="")
    print("")
