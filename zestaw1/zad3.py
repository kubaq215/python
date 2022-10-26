import math

print("Enter length: ", end="")
a = input()
a = int(a)
one_click = '|....'
my_string = ''
for i in range(a):
    my_string += one_click
my_string += '|\n'
my_string += '0'
k = 1
i = 1
while(i < a*5+1):
    p = int(math.log10(k))
    if (i+p)%5 == 0:
        my_string += str(k)
        k+=1
        i+=p
    else:
        my_string += " "
    i+=1
print(my_string)