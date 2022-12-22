map = {}
dirs = [1, 1j, -1, -1j]
max_x = 0
max_y = 0


def new_dir(dir_idx: int, rotation: str):
    if rotation == 'R':
        return (dir_idx + 1) % 4
    else:
        return (dir_idx - 1) % 4


def wrap_around(curr_pos, inc):
    # print("starting pos for wrap:", curr_pos)
    if inc == 1:
        next_pos = complex(0, curr_pos.imag)
        square = map.get(next_pos)
        while square is None:
            next_pos += inc
            square = map.get(next_pos)
        # print("wrapping around to:", next_pos)
        return next_pos
    elif inc == -1:
        next_pos = complex(max_x, curr_pos.imag)
        square = map.get(next_pos)
        while square is None:
            next_pos += inc
            square = map.get(next_pos)
        # print("wrapping around to:", next_pos)
        return next_pos
    elif inc == 1j:
        next_pos = complex(curr_pos.real, 0)
        square = map.get(next_pos)
        while square is None:
            next_pos += inc
            square = map.get(next_pos)
        # print("wrapping around to:", next_pos)
        return next_pos
    elif inc == -1j:
        next_pos = complex(curr_pos.real, max_y)
        square = map.get(next_pos)
        while square is None:
            next_pos += inc
            square = map.get(next_pos)
        # print("wrapping around to:", next_pos)
        return next_pos


def move(curr_pos, dir_idx, rotation, dist):

    if rotation == 'S':
        inc = 1
        new_dir_idx = dir_idx
    else:
        new_dir_idx = new_dir(dir_idx, rotation)
        inc = dirs[new_dir_idx]
    # print("direction to walk next:", inc)
    # print("new starting position:", curr_pos)

    while dist > 0:
        # print(curr_pos)
        next_pos = curr_pos + inc
        # print("next position to check:", next_pos)
        square = map.get(next_pos)
        if square is None:
            # print("out of bounds, wrap around")
            next_pos = wrap_around(next_pos, inc)
            # print(curr_pos)
            square = map.get(next_pos)
            if square == '#':
                print("hit wall")
                break
            else:
                curr_pos = next_pos
            print("going to:", curr_pos, "instead")
        elif square == '#':
            # print("hit wall")
            break
        else:
            curr_pos = next_pos
            # print("moving to next square")
        # print(curr_pos)
        dist -= 1
    return curr_pos, new_dir_idx


with open('./data.txt', 'r') as data:
    lines = data.readlines()
    inst = list(lines[-1][:-1])
    x: int
    y: int
    for y, line in enumerate(lines[:-2]):
        for x, c in enumerate(line[:-1]):
            key = complex(x, y)
            map[key] = c
            max_x = max(max_x, x)
            max_y = max(max_y, y)
max_x += 2
max_y += 2

keys = list(map.keys())
for k in keys:
    if map[k] == ' ':
        map.pop(k)

# for k, v in map.items():
#     print(k, v)

print(max_x, max_y)
dist = ''
dir = 'S'
instructions = []

for c in inst:
    if c.isnumeric():
        dist += c
    else:
        instructions.append((dir, int(dist)))
        dir = c
        dist = ''

instructions.append((dir, int(dist)))
print(instructions[0], instructions[-1])

dir_idx = 0
# manually find and set starting position
position = 50
########

print(map.get(50))
for instruction in instructions:
    rotation, dist = instruction
    position, dir_idx = move(position, dir_idx, rotation, dist)


print("final position:", position, "and final direction:", dir_idx)
final_sum = (position.imag + 1) * 1000 + (position.real + 1) * 4 + dir_idx
print("final sum:", int(final_sum))
