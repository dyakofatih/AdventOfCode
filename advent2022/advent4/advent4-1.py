
fully_assigned = 0

with open("./data.txt", "r") as data:
    for line in data.readlines():
        sections = line[:-1].split(",")
        # print(sections[0], sections[1])
        range_1 = sections[0].split("-")
        range_2 = sections[1].split("-")
        # print(range_1, range_2)

        lower_1 = int(range_1[0])
        upper_1 = int(range_1[1])

        lower_2 = int(range_2[0])
        upper_2 = int(range_2[1])

        if lower_1 >= lower_2 and upper_1 <= upper_2:
            fully_assigned += 1
            continue 
        elif lower_2 >= lower_1 and upper_2 <= upper_1:
            fully_assigned += 1



print(fully_assigned, "pairs have fully contained subset")