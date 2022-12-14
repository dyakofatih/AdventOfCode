with open("./data.txt", "r") as data:

    line = data.readline()

    up = line.count("(")
    down = line.count(")")

    print(up - down)
