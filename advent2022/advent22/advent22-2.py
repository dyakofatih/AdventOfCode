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
    if inc == 1:  # out of bounds to the right
        if 1 <= curr_pos.imag <= 50:  # R2 -> R5
            next_pos = complex(100, 151 - curr_pos.imag)
            inc = -1
            return next_pos, inc
        elif 51 <= curr_pos.imag <= 100:  # R3 -> B2
            next_pos = complex(50 + curr_pos.imag, 50)
            inc = -1j
            return next_pos, inc
        elif 101 <= curr_pos.imag <= 150:  # R5 -> R2
            next_pos = complex(150, 151 - curr_pos.imag)
            inc = -1
            return next_pos, inc
        elif 151 <= curr_pos.imag <= 200:  # R6 -> B5
            next_pos = complex(curr_pos.imag - 100, 150)
            inc = -1j
            return next_pos, inc
    elif inc == -1:  # out of bounds to the left
        if 1 <= curr_pos.imag <= 50:  # L1 -> L4
            next_pos = complex(1, 151 - curr_pos.imag)
            inc = 1
            return next_pos, inc
        elif 51 <= curr_pos.imag <= 100:  # L3 -> T4
            next_pos = complex(curr_pos.imag - 50, 101)
            inc = 1j
            return next_pos, inc
        elif 101 <= curr_pos.imag <= 150:  # L4 -> L1
            next_pos = complex(51, 151 - curr_pos.imag)
            inc = 1
            return next_pos, inc
        elif 151 <= curr_pos.imag <= 200:  # L6 - T1
            next_pos = complex(curr_pos.imag - 100, 1)
            inc = 1j
            return next_pos, inc
    elif inc == 1j:  # out of bounds downwards
        if 1 <= curr_pos.real <= 50:  # B6 -> T2
            next_pos = complex(curr_pos.real + 100, 1)
            inc = 1j
            return next_pos, inc
        elif 51 <= curr_pos.real <= 100:  # B5 -> R6
            next_pos = complex(50, curr_pos.real + 100)
            inc = -1
            return next_pos, inc
        elif 101 <= curr_pos.real <= 150:  # B2 -> R3
            next_pos = complex(100, curr_pos.real - 50)
            inc = -1
            return next_pos, inc
    elif inc == -1j:  # out of bounds to to the top
        if 1 <= curr_pos.real <= 50:  # T4 -> L3
            next_pos = complex(51, curr_pos.real + 50)
            inc = 1
            return next_pos, inc
        elif 51 <= curr_pos.real <= 100:  # T1 -> L6
            next_pos = complex(1, 100 + curr_pos.real)
            inc = 1
            return next_pos, inc
        elif 101 <= curr_pos.real <= 150:  # T2 -> B6
            next_pos = complex(curr_pos.real - 100, 200)
            inc = -1j
            return next_pos, inc


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
            wrap_pos, tmp_inc = wrap_around(next_pos, inc)
            # print(inc, tmp_inc)
            # print(curr_pos, next_pos, wrap_pos)
            # print(curr_pos)
            square = map.get(wrap_pos)
            # print(square)
            if square == '#':
                # print("hit wall")
                break
            # elif square is None:
            #     print("ERROR!!!!!!!!1")
            #     exit()
            else:
                curr_pos = wrap_pos
                inc = tmp_inc
                new_dir_idx = dirs.index(inc)
            # print("going to:", curr_pos, "instead")
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
            key = complex(x+1, y+1)
            map[key] = c

keys = list(map.keys())
for k in keys:
    if map[k] == ' ':
        map.pop(k)

# for k, v in map.items():
#     print(k, v)

# print(max_x, max_y)
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
# print(instructions[0], instructions[-1])

dir_idx = 0
# starting point for real data
position = (51 + 1j)
##############################
# starting point for test data
# position = (9 + 1j)
##############################

# print(map.get((51 + 1j)))
for instruction in instructions:
    rotation, dist = instruction
    position, dir_idx = move(position, dir_idx, rotation, dist)


print("final position:", position, "and final direction:", dir_idx)
final_sum = position.imag * 1000 + position.real * 4 + dir_idx
print("final sum:", int(final_sum))
