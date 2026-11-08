s = input().split()
X = int(s[0])
Y = int(s[1])

if Y % X == 0:
    print(X + Y)
else:
    print(Y - X)
