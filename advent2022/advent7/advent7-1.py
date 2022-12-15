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

for x, y in dirDict.items():
    for k, v in dirDict.items():

        if x == k:
            ...
        elif x == k[:len(x)]:
            y += v

    dirDict.update({x : y})

print(dirDict)

sum = 0
for x in dirDict.values():
    if x <= 100000:
        sum += x

print(sum)