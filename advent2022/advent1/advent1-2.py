import heapq as hp

calSums = []
currCal = 0
with open("./data.txt", "r") as d:
    for data in d.readlines():
        if data != "\n":
            currCal += int(data)
        else:
            hp.heappush(calSums, currCal)
            currCal = 0

top3 = sum(hp.nlargest(3, calSums))
print(top3)