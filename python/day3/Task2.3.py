for i in range(10000, 0, -1):
    if i % 7 == 0:
        print(i)

[print(i) for i in range(10000, 0, -1) if i % 7 == 0]
