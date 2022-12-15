
has_overlap = 0

with open("./data.txt", "r") as data:
    for line in data.readlines():
        sections = line[:-1].split(",")

        range_1 = sections[0].split("-")
        range_2 = sections[1].split("-")

        lower_1 = int(range_1[0])
        upper_1 = int(range_1[1])

        lower_2 = int(range_2[0])
        upper_2 = int(range_2[1])

        if upper_1 >= lower_2 and lower_1 <= upper_2:
            has_overlap += 1
        
print(has_overlap)