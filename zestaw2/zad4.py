print("x = ", end="")
x = input()
print("y = ", end="")
y = input()
print("z = ", end="")
z = input()
print("n = ", end="")
n = input()

l = []

for i in range(int(x)+1):
    for j in range(int(y)+1):
        for k in range(int(z)+1):
            if i + j + k != int(n):
                l.append([i,j,k])

print(l)
