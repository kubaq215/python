def fun(set1, set2):
    c = set1.union(set2)      
    d = set1.intersection(set2)
    print("A -", set1)
    print("B -", set2)
    print("A\u222AB -" , c)
    print("A\u2229B -", d)

a = {1, 2, 3}
b = {3, 4, 5}
fun(a, b)
print("")
a = {"a", "b", "c", "d"}
b = {"e", "f", "b", "a"}
fun(a, b)