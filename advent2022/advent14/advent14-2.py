
def rockwall(nodes: list[tuple[int, int]], formation: set[tuple[int, int, str]]) -> set[tuple[int, int, str]]:
    # print(len(nodes))
    for i in range(len(nodes) - 1):
        node1 = nodes[i]
        node2 = nodes[i+1]
        # print(node1[0] == node2[0])
        if node1[0] == node2[0]:
            formation.update({(node1[0], y) for y in (range(
                node1[1], node2[1] + 1) if node1[1] < node2[1] else range(node2[1], node1[1] + 1))})
        else:
            formation.update({(x, node1[1]) for x in (range(
                node1[0], node2[0] + 1) if node1[0] < node2[0] else range(node2[0], node1[0] + 1))})
    return formation


def parse_formation(input: str) -> set[tuple[int, int, str]]:
    formation: set[tuple[int, int, str]] = set()
    with open(input, 'r') as data:
        for line in data:

            # print(line)
            line: list[str] = line.replace(' -> ', ',').split(',')
            # print(line)

            nodes: list[int] = [(int(line[i]), int(line[i+1]))
                                for i in range(0, len(line), 2)]
            # print(nodes)
            formation.update(rockwall(nodes, formation))
            # print(formation)
    return formation


def find_edge_of_formation(formation: set[tuple[int, int, str]]) -> tuple[int, int, int]:

    l, _ = min(formation, key=lambda x: x[0])
    r, _ = max(formation, key=lambda x: x[0])
    _, b = max(formation, key=lambda x: x[1])
    print("left most pos:", l)
    print("right most pos:", r)
    print("bottom most pos:", b)

    return l, r, b


def drop_one_grain(formation: set[tuple[int, int, str]], bottom: int) -> bool:
    sand: list[int] = [500, 0]

    can_fall: bool = True
    while can_fall:
        # print(sand)
        if (sand[0], sand[1] + 1) not in formation and sand[1] + 1 != bottom:
            sand[1] += 1
        elif (sand[0] - 1, sand[1] + 1) not in formation and sand[1] + 1 != bottom:
            sand[0] -= 1
            sand[1] += 1
        elif (sand[0] + 1, sand[1] + 1) not in formation and sand[1] + 1 != bottom:
            sand[0] += 1
            sand[1] += 1
        elif (sand[0], sand[1]) in formation:
            return True
        else:
            can_fall = False
    formation.update({(sand[0], sand[1])})
    return False


def generate_cave(formation, bottom):
    height = bottom + 2
    width = 2 * height + 1
    offset = 500 - width // 2
    cave = [[' ' for _ in range(width)]
            for _ in range(height)]
    for rock in formation:
        cave[rock[1]][rock[0] - offset] = '#'
    cave.append(['#' for _ in range(width)])
    return cave


def add_sand_to_cave(cave, bottom):
    height = bottom + 2
    width = 2 * height + 1
    offset = 500 - width // 2
    for sand in formation:
        cave[sand[1]][sand[0] - offset] = '.' if cave[sand[1]][sand[0] -
                                                               offset] != '#' else '#'
    return cave


formation: set[tuple[int, int, str]] = parse_formation("data.txt")
# print(formation)


left, right, bottom = find_edge_of_formation(formation)
cave = generate_cave(formation, bottom)
# for row in cave:
#     print(''.join(row))
reached_top: bool = False
grains_of_sand: int = 0
while not reached_top:
    # "bottom + 2" is used to simulate the bottom floor
    reached_top = drop_one_grain(formation, bottom + 2)
    grains_of_sand += 1 if not reached_top else 0
    # print(formation)
# cave = generate_cave(formation, bottom)
cave = add_sand_to_cave(cave, bottom)
for row in cave:
    print(''.join(row))
print(reached_top)
print(grains_of_sand)
