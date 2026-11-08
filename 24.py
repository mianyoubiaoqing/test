s = input().split()
a = int(s[0])
b = int(s[1])

count = 0
for i in range(a, b + 1):
    digit_sum = 0
    for ch in str(i):
        digit_sum = digit_sum + int(ch)

    if digit_sum > 0 and digit_sum % 5 == 0:
        count = count + 1

print(count)
