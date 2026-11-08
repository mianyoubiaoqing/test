s = input().split()
n = int(s[0])
k = int(s[1])
m = int(s[2])

people = []
for i in range(n):
    people.append(i)

index = k
while len(people) > 1:
    index = (index + m - 1) % len(people)
    people.pop(index)

print(people[0])
