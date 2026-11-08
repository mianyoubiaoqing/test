s = input().split()
n = int(s[0])
x = s[1]

ans = 0
for i in range(1, n + 1):
    ans = ans + str(i).count(x)

print(ans)
