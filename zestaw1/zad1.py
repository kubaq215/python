print("Enter the width: ")
a = input()
a = int(a)
for i in range(a // 2 + 1):
    print("")
    for j in range(a):
        if i == 0:
            print("*", end="")
            continue
        if i != a // 2:
            if j == a - i-1 or j == i:
                print("*", end="")
            else: 
                print(" ", end="")
            continue
        if j != a//2:
            print(" ", end="")
        else:
            print("*")