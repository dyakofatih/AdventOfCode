def read_map(path):
    with open(path, "r") as data:
        map_of_trees = [ [int(x) for x in line[:-1]] for line in data ]

    return map_of_trees


def counting_trees(m): # map_of_trees

    rnge = len(m)
    t_m = [[row[i] for row in m] for i in range(len(m[0]))]
    trees = [['u' for _ in range(rnge)] for _ in range(rnge)]
    hidden = 0

    ## (1) check if hidden from left view 
    for x in range(1, rnge - 1):

        for y in range(1, rnge - 1):
            if m[x][y] <=  max(m[x][:y]):
                trees[x][y] = 'h'
            else:
                trees[x][y] = 'v'
    
    # (2) check if hidden from right view 
    for x in range(1, rnge - 1):
        for y in range(1, rnge - 1):
            if m[x][y] <=  max(m[x][y+1:]) and trees[x][y] != 'v':
                trees[x][y] = 'h'
            else:
                trees[x][y] = 'v'

    # using a transposed list for (3) and (4)

    ## check if hidden from top view, samme as (1) but with 
    for x in range(1, rnge - 1):
        for y in range(1, rnge - 1):
            if t_m[x][y] <=  max(t_m[x][:y]) and trees[y][x] != 'v':
                trees[y][x] = 'h'
            else:
                trees[y][x] = 'v'

    ## check if hidden from bottom view same as (2) but with transposed 
    for x in range(1, rnge - 1):
        for y in range(1, rnge - 1):
            if t_m[x][y] <=  max(t_m[x][y+1:]) and trees[y][x] != 'v':
                trees[y][x] = 'h'
            else:
                trees[y][x] ='v'

    for row in trees:
        hidden += row.count('h')

    return trees, hidden



map_of_trees = read_map("./data.txt")
t_m = [[row[i] for row in map_of_trees] for i in range(len(map_of_trees[0]))]

for row in map_of_trees:
    print(row)

print(" ")

map_of_hidden, hidden = counting_trees(map_of_trees)


print("there are {} hidden trees".format(hidden))
print("there are {} visible trees trees".format( len(map_of_trees)**2 - hidden ))

for row in map_of_hidden:
    print(row)