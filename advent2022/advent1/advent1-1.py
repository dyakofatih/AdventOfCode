maxCal  = 0
currCal = 0
with open("./data.txt", "r") as d:
    for data in d.readlines():
        if data != "\n":
            currCal += int(data)
        else:
            maxCal = max(maxCal,currCal)
            currCal = 0

print(maxCal)

