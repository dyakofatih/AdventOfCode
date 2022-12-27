moves = [-1j, 1j, -1, 1]
precheck: list[complex] = [-1, -1-1j, -1j, 1-1j, 1, 1+1j, 1j, -1+1j]
FoV: list[list[complex]] = [[-1-1j, -1j, 1-1j],  # North
                            [1+1j, 1j, -1+1j],   # South
                            [-1, -1-1j, -1+1j],  # East
                            [1-1j, 1, 1+1j]]     # West

# key is the elf's current coordinate,
# the first value is the index of thr first direction to check on the next round,
# the second value will hold the proposed coordinate of the elf if it is going to move
elves: dict[complex, list[int, complex]] = dict()
proposed_moves: dict[complex, int] = dict()
with open('./data_test.txt', 'r') as data:
    lines = data.readlines()

    for y, line in enumerate(lines, start=1):
        for x, c in enumerate(line[:-1], start=1):
            if c == '#':
                # print(f'elf at coordinate: ({x}, {y})')
                cord: complex = complex(x, y)
                elves[cord] = [0, None]


def any_neighbours(elf: complex) -> bool:
    for dir in precheck:
        if elves.get(elf+dir) is not None:
            return True
    else:
        return False


def propose_move(elf: complex) -> bool:
    # given a direction and an elf, if the direction is clear,
    # return true and generate a proposed coordinate, else return false
    dir_idx, proposed_cord = elves.get(elf)
    to_check = FoV[dir_idx]
    for step in to_check:
        if elves.get(elf+step) is not None:
            dir_idx = (dir_idx + 1) % 4
            elves[elf] = [dir_idx, proposed_cord]
            return False
    proposed_cord = elf+moves[dir_idx]
    dir_idx = (dir_idx + 1) % 4

    no_of_elves = proposed_moves.get(proposed_cord)
    if no_of_elves is None:
        proposed_moves[proposed_cord] = 1
    else:
        proposed_moves[proposed_cord] = no_of_elves + 1

    elves[elf] = [dir_idx, proposed_cord]
    return True


def check_sides(elf: complex):
    for _ in range(4):
        if propose_move(elf):
            break


def move(elf: complex):
    dir_idx, proposed_cord = elves.get(elf)

    if proposed_cord is None:
        pass
    elif proposed_moves.get(proposed_cord) > 1:
        elves[elf] = [dir_idx, None]
    elif proposed_moves.get(proposed_cord) == 1:
        elves.pop(elf)
        print("after pop:", len(elves))
        if proposed_cord in elves:
            print("WTF?!?!?!?!")
        elves[proposed_cord] = [dir_idx, None]
        print("after adding new coord:", len(elves))


for elf, val in elves.items():
    print(elf)
for _ in range(10):

    for elf in elves.keys():
        has_neighbours: bool = any_neighbours(elf)
        if has_neighbours:
            check_sides(elf)

    print(len(elves))

    keys = list(elves.keys())
    for elf in keys:
        move(elf)
    proposed_moves.clear()

    # print(len(elves))


print("after 10 round:")
for elf, val in elves.items():
    print(elf)
