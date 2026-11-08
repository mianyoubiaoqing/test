s = input().split()
L = int(s[0])
M = int(s[1])

trees = [1] * (L + 1)

for i in range(M):
    line = input().split()
    left = int(line[0])
    right = int(line[1])

    for pos in range(left, right + 1):
        trees[pos] = 0

ans = 0
for x in trees:
    ans = ans + x

print(ans)
