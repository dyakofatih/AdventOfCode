import sys
import math

sum = 0
dirDict = {}
currDir = "/"


### build tree
with open("./data.txt", "r") as data:
    _ = data.readline()

    dirDict.update({"/": 0})
    for x in data:

        line = x[:-1].split(" ")
        if len(line) == 3:
            if line[2] != "..":
                currDir += line[2] + "/"
                dirDict.update({currDir[:-1]: 0})
            else:
                currDir = currDir[:currDir[:-1].rfind("/") + 1]



currDir = "/"
with open("./data.txt", "r") as data:
    _ = data.readline()

    dirDict.update({"/": 0})
    for x in data.readlines():
        line = x[:-1].split(" ")
        
        if line[1] != "ls" and line[1] != "cd":
            if line[0].isnumeric():
                if currDir == "/":
                    dirDict.update({currDir : dirDict[currDir] + int(line[0])})
                else:
                    dirDict.update({currDir[:-1] : dirDict[currDir[:-1]] + int(line[0])})

        if len(line) == 3:
            if line[2] != "..":
                currDir += line[2] + "/"
                
            if line[2] == "..":
                currDir = currDir[:currDir[:-1].rfind("/") + 1]

print(len(dirDict.items()))

sum = 0
for x in dirDict.values():
        sum += x

print("total disk usage:", sum)

disk_volume = 70000000

required_free_space = 30000000

max_space = disk_volume - required_free_space

overshoot = sum - max_space

min_to_clear_overshoot = 9999999999

print("need to remove:", overshoot)

for x, y in dirDict.items():
    for k, v in dirDict.items():

        if x == k:
            ...
        elif x == k[:len(x)]:
            y += v

    dirDict.update({x : y})

for x in dirDict.values():
    if x >= overshoot:
        min_to_clear_overshoot = min(x, min_to_clear_overshoot)

print("smalled directory to free up enough space:", min_to_clear_overshoot)





 