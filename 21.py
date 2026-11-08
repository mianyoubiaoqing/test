s = input().split()
L = int(s[0])
R = int(s[1])

ans = 0
for i in range(L, R + 1):
    ans = ans + str(i).count("2")

print(ans)
