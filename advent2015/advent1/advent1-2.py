with open("./data.txt", "r") as data:

    current_floor = 0
    for i, char in enumerate(iterable=data.readline(), start=1):
        current_floor += 1 if char == '(' else -1
        if current_floor == -1:
            print(i)
            break
