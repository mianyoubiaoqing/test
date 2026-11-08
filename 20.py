n = int(input())
s = input().split()

a = []
for i in range(n):
    a.append(int(s[i]))

last = a[n - 1]

if last == 0:
    print("UP")
elif last == 15:
    print("DOWN")
elif n == 1:
    print("-1")
elif a[n - 1] > a[n - 2]:
    print("UP")
else:
    print("DOWN")
