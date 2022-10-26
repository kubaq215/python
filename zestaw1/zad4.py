import sys 

argv = sys.argv[1:]
numbers = [int(x) for x in argv]

h = numbers[0] * 2 + 1
d = numbers[1] * 2 + 1
for i in range(h):
    for j in range(d):
        if i == 0 or i == h-1:
            if j%2 == 0: print('+', end="")
            else: print('-', end="")
        elif j == 0 or j == d-1:
            if i%2 == 1: print('|', end="")
            else: print('+', end="")
        elif i%2 == 1:
            if j%2 == 0: print('|', end="")
            else: print(" ", end="")
        else:
            if j%2 == 1: print("-", end="")
            else: print("+", end="")
    print("")

