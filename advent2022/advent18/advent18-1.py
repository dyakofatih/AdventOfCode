from time import perf_counter


cubes: set[tuple[int, ...]] = set()

sides: list[list[int]] = [[-1, 0, 0], [1, 0, 0],
                          [0, -1, 0], [0, 1, 0], [0, 0, -1], [0, 0, 1]]

with open('./data.txt', 'r') as data:
    for line in data:
        x, y, z = line[:-1].split(',')
        cubes.update({(int(x), int(y), int(z))})

start: int = perf_counter()
free_sides: int = 0
for cube in cubes:
    for side in sides:
        gen_adjecent = tuple([c+s for c, s in zip(cube, side)])

        if gen_adjecent not in cubes:
            free_sides += 1

print(perf_counter() - start)
print(free_sides)
