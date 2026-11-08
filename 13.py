ch = input().strip()
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n = letters.index(ch) + 1

for i in range(n):
    line = " " * (n - 1 - i)
    for j in range(i + 1):
        line = line + letters[j]
    for j in range(i - 1, -1, -1):
        line = line + letters[j]
    print(line)
