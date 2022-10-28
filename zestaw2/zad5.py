def fun(N):
    max = 0
    spots = [i for i, num in enumerate(str(bin(N))) if num == '1']
    if len(spots) < 2:
        return 0
    for i in range(len(spots)-1):
        if max < spots[i+1] - spots[i] - 1: 
            max = spots[i+1] - spots[i] - 1
    return max

print(fun(529))