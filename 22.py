while True:
    try:
        s = input().split()
        if len(s) == 0:
            break
    except:
        break

    y = int(s[0])
    m = int(s[1])
    x = s[2]

    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        days = 31
    elif m == 4 or m == 6 or m == 9 or m == 11:
        days = 30
    else:
        if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
            days = 29
        else:
            days = 28

    total = 0
    for d in range(1, days + 1):
        date_str = "%04d-%02d-%02d" % (y, m, d)
        total = total + date_str.count(x)

    print(total)
