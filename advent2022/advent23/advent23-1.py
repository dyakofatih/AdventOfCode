N = 1j
S = -1j
W = -1
E = 1
NW = N + W
NE = N + E
SW = S + W
SE = S + E

moves = [N, S, W, E]
precheck: list[complex] = [N, S, E, W, NW, NE, SW, SE]
FoV: list[list[complex]] = [[N, NE, NW],  # North
                            [S, SE, SW],  # South
                            [W, NW, SW],  # West
                            [E, NE, SE]]  # Eest

# key is the elf's current coordinate,
# the first value is the index of thr first direction to check on the next round,
# the second value will hold the proposed coordinate of the elf if it is going to move
elves: dict[complex, list[int, complex]] = dict()
proposed_moves: dict[complex, int] = dict()
with open('./data.txt', 'r') as data:
    lines = data.readlines()
    print(len(lines))
    for y, line in enumerate(lines[::-1]):

        for x, c in enumerate(line.strip()):
            if c == '#':
                # print(f'elf at coordinate: ({x}, {y})')
                cord: complex = complex(x, y)
                elves[cord] = [0, None]


def any_neighbours(elf: complex) -> bool:
    for dir in precheck:
        # print(elf, dir)
        if elves.get(elf+dir) is not None:
            # print(elves.get(elf+dir))
            return True
        assert elves.get(elf+dir) is None
    else:
        return False


def propose_move(elf: complex, offset: int) -> bool:
    # given a direction and an elf, if the direction is clear,
    # return true and generate a proposed coordinate, else return false
    dir_idx, proposed_cord = elves.get(elf)

    assert 0 <= dir_idx <= 3
    direction_to_check_idx = (dir_idx + offset) % 4
    assert 0 <= direction_to_check_idx <= 3

    for step in FoV[direction_to_check_idx]:
        if elves.get(elf+step) is not None:
            return False

    # print("elf {}, propose to move to {}, as {} are clear".format(
    #     elf, elf + moves[direction_to_check_idx], [elf + move for move in FoV[direction_to_check_idx]]))

    proposed_cord = elf+moves[direction_to_check_idx]
    no_of_elves = proposed_moves.get(proposed_cord)
    if no_of_elves is None:
        proposed_moves[proposed_cord] = 1
    else:
        assert no_of_elves > 0 and no_of_elves is not None
        proposed_moves[proposed_cord] = no_of_elves + 1

    assert proposed_cord is not None
    elves[elf] = [dir_idx, proposed_cord]
    return True


def check_sides(elf: complex):
    for i in range(4):
        if propose_move(elf, offset=i):
            break


def move(elf: complex):
    dir_idx, proposed_cord = elves.get(elf)
    assert isinstance(dir_idx, int)
    # print(dir_idx)
    dir_idx = (dir_idx + 1) % 4
    assert 0 <= dir_idx <= 3
    if proposed_cord is None:
        elves[elf] = [dir_idx, None]
        return
    elif proposed_moves.get(proposed_cord) > 1:
        elves[elf] = [dir_idx, None]
        return
    elif proposed_moves.get(proposed_cord) == 1:
        elves.pop(elf)
        assert proposed_cord not in elves
        elves[proposed_cord] = [dir_idx, None]
        assert elves.get(elf) is None
        return

    assert False  # should not end up here ever


number_of_elves = len(elves)
for i in range(10):
    print("round:", i+1)
    for elf in elves.keys():
        has_neighbours: bool = any_neighbours(elf)
        if has_neighbours:
            check_sides(elf)

    # print(len(elves))

    for elf in elves.keys():
        dir_idx, _ = elves.get(elf)
        assert dir_idx == i % 4

    keys = list(elves.keys())
    for elf in keys:
        move(elf)

    proposed_moves.clear()
    assert len(proposed_moves) == 0
    assert len(elves) == number_of_elves


print("after 10 round:")
# for elf, val in elves.items():
#     print(elf)
max_x = max(*elves.keys(), key=lambda n: n.real).real
min_x = min(*elves.keys(), key=lambda n: n.real).real

max_y = max(*elves.keys(), key=lambda n: n.imag).imag
min_y = min(*elves.keys(), key=lambda n: n.imag).imag

print(max_x, min_x, max_y, min_y)

area = abs(max_x - min_x + 1) * abs(max_y - min_y + 1)
print(area, number_of_elves)
free_area = area - number_of_elves
print("there are {} free squares between the elves".format(free_area))
