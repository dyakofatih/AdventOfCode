cubes: set[tuple[int, ...]] = set()

sides: list[list[int]] = [[-1, 0, 0], [1, 0, 0],
                          [0, -1, 0], [0, 1, 0], [0, 0, -1], [0, 0, 1]]

with open('./data.txt', 'r') as data:
    for line in data:
        x, y, z = line[:-1].split(',')
        cubes.update({(int(x), int(y), int(z))})

min_x = min(x[0] for x in cubes)
min_y = min(x[1] for x in cubes)
min_z = min(x[2] for x in cubes)
max_x = max(x[0] for x in cubes)
max_y = max(x[1] for x in cubes)
max_z = max(x[2] for x in cubes)

min_v = min(min_x, min_y, min_z) - 2
max_v = max(max_x, max_y, max_z) + 2

print(min_v, max_v)


def flood_fill(s_c: tuple[int, ...], b_c: dict[tuple[int, ...], bool]):

    queue: list[tuple[int, ...]] = list()

    queue.append(s_c)

    while queue:
        e_c = queue.pop(0)
        b_c[e_c] = True

        for side in sides:
            cube = tuple([s+c for s, c in zip(side, e_c)])
            if cube in b_c and not b_c[cube] and cube not in queue:
                queue.append(cube)


free_sides: int = 0
for cube in cubes:
    for side in sides:
        gen_adjecent = tuple([c+s for c, s in zip(cube, side)])

        if gen_adjecent not in cubes:
            free_sides += 1

bounding_cube: dict[tuple[int, ...], bool] = dict()
for x in range(min_v, max_v):
    for y in range(min_v, max_v):
        for z in range(min_v, max_v):
            if (x, y, z) not in cubes:
                bounding_cube[(x, y, z)] = False

s_c: tuple[int, ...] = (min_v, min_v, min_v)

flood_fill(s_c, bounding_cube)
pockets: set[tuple[int, ...]] = set(
    [cube for cube in bounding_cube if not bounding_cube[cube]])
pocket_area: int = 0
for pocket in pockets:
    for side in sides:
        gen_adjecent = tuple([c+s for c, s in zip(pocket, side)])

        if gen_adjecent not in pockets:
            pocket_area += 1

print(free_sides, len(cubes))
print(pocket_area, len(pockets))
print(free_sides - pocket_area)
