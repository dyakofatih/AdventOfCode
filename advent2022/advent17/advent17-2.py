from itertools import cycle
from time import perf_counter

horizontal_bar: list[complex] = [0, 1, 2, 3]
plus: list[complex] = [1, 1j, 2 + 1j, 1 + 2j]
inverse_L: list[complex] = [0, 1, 2, 2 + 1j, 2 + 2j]
vertical_bar: list[complex] = [0, 1j, 2j, 3j]
square: list[complex] = [0, 1, 0 + 1j, 1 + 1j]

with open('data.txt', 'r') as data:
    moves = cycle(data.readline()[:-1])
shapes = cycle([horizontal_bar, plus, inverse_L, vertical_bar, square])

# check if moving the rock in the jet's direction will make it collide with either
# any part of the formation or the walls.


def move_if_no_collision(rock: set[complex], jet: str) -> set[complex]:
    tmp: set[complex] = {r - 1 if jet == '<' else r + 1 for r in rock}
    if not tmp & formation and all(0 <= r.real < 7 for r in tmp):
        return tmp
    else:
        return rock


def rock_falling(formation: set[complex], rock: set[complex]) -> bool:
    rock = {r - 1j for r in rock}
    if formation & rock:
        return False
    return True


# initial rock formation, 7 unit wide flat surface at height -1
formation: set[complex] = {-1j, 1 - 1j, 2 - 1j, 3 - 1j, 4 - 1j, 5 - 1j, 6 - 1j}
elevation = 0

cache: dict = dict()


##########
rocks = 72+1745  # number of rocks to simulate
##########
inc: str = ''
s = perf_counter()
for i in range(rocks):
    # Get rock from shapes and shift up with 3 over current elevation
    # and left with 2
    rock = {r + 2 + (elevation + 3) * 1j for r in next(shapes)}
    falling: bool = True

    while falling:
        jet: str = next(moves)
        rock: set[complex] = move_if_no_collision(rock, jet)

        falling = rock_falling(formation, rock)
        if not falling:
            formation = formation | rock
            old_elevation = elevation
            elevation = max(r.imag for r in formation) + 1
            inc += str(int(elevation - old_elevation))
        else:
            rock = {r - 1j for r in rock}

print(perf_counter() - s)
print(elevation)

with open('./data_test.txt', 'w') as output:
    print(inc)
    output.write(inc)
