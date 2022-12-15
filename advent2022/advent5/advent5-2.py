crate_stacks = ["", "", "", "", "", "", "", "", ""]
with open("./data.txt", "r") as data:
    for line in data.readlines(275):
        row = line[:-1]
        crate_stacks[0] += row[1] if row[1] != " " else ""
        for crate in range(1, 9):
            crate_stacks[crate] += row[crate*4+1] if row[crate*4+1] != " " else ""
    data.readlines(36)
    for line in data.readlines():
        step = []
        move = line[:-1].split(" ")
        step.append(int(move[1]))
        step.append(int(move[3]))
        step.append(int(move[5]))
        crate_stacks[step[2] - 1] = crate_stacks[step[1] - 1][:step[0]] + crate_stacks[step[2] - 1]
        crate_stacks[step[1] - 1] = crate_stacks[step[1] - 1][step[0]:]
[print(i[0], end="") for i in crate_stacks]