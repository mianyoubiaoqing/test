while True:
    try:
        n = int(input())
    except:
        break

    for i in range(1, n + 2):
        spaces = " " * (2 * (n + 1 - i))
        stars = "*" * i
        print(spaces + stars)

    for i in range(n, 0, -1):
        spaces = " " * (2 * (n + 1 - i))
        stars = "*" * i
        print(spaces + stars)
