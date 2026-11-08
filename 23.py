s = input().strip()

rev = ""
for i in range(len(s) - 2, -1, -1):
    rev = rev + s[i]

num = int(s + rev)

is_prime = True
i = 2
while i * i <= num:
    if num % i == 0:
        is_prime = False
        break
    i = i + 1

if is_prime:
    print("prime")
else:
    print("noprime")
