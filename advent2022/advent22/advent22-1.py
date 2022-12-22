map = []


with open('./data_test.txt', 'r') as data:
    lines = data.readlines()
    instructions = lines[-1]
    for line in lines[:-2]:
        r = []
        for c in line[:-1]:
            r.append(c)
        map.append(r)
        print(r)
print(instructions)


def move(curr_pos, curr_dir, dir, dist):
    ...
