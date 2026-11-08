T = int(input())

for k in range(T):
    n = int(input())
    s = input().split()

    a = []
    for i in range(n):
        a.append(int(s[i]))

    max_val = a[0]
    min_val = a[0]
    total = 0
    for x in a:
        if x > max_val:
            max_val = x
        if x < min_val:
            min_val = x
        total = total + x

    ji_cha = max_val - min_val
    avg = total / n

    sq_sum = 0
    for x in a:
        sq_sum = sq_sum + (x - avg) * (x - avg)
    fang_cha = sq_sum / n

    print("%d %.3f" % (ji_cha, fang_cha))
