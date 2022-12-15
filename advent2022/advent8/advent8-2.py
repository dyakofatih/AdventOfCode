def read_map(path):
    with open(path, "r") as data:
        map_of_trees = [ [int(x) for x in line[:-1]] for line in data ]

    return map_of_trees


def counting_trees(m): # map_of_trees

    rnge = len(m)
    print(rnge, len(m[0]))
    t = [[row[i] for row in m] for i in range(len(m[0]))]
    tree_scores =   [ [ 1 for _ in range(rnge)] for _ in range(rnge) ]

    r_test=3
    c_test=2

    for r in range(1, rnge - 1):

        for c in range(1, rnge - 1):

            curr_tree_height = m[r][c] 

            # check view to the left
            for i in range(1, rnge):
                if c - i == 0 or curr_tree_height <= m[r][c - i] :
                    tree_scores[r][c] *= i
                    if r == r_test and c == c_test:
                        print(i)
                    break


            # check view to the top
            for i in range(1, rnge):
                if r - i == 0 or curr_tree_height <= t[c][r - i] :
                    tree_scores[r][c] *= i
                    if r == r_test and c == c_test:
                        print(i)
                    break

            # check view to the right
            for i in range(1, rnge):
                if c + i + 1 == rnge or curr_tree_height <= m[r][c + i] :
                    tree_scores[r][c] *= i
                    if r == r_test and c == c_test:
                        print(i)
                    break

            # check view to the bottom
            for i in range(1, rnge):
                if r + i + 1 == rnge or curr_tree_height <= t[c][r + i] :
                    tree_scores[r][c] *= i
                    if r == r_test and c == c_test:
                        print(i)
                    break
            
                        
    return tree_scores



map_of_trees = read_map("./data.txt")
test_transpose = [[row[i] for row in map_of_trees] for i in range(len(map_of_trees[0]))]

for row in map_of_trees:
    print(row)
print(" ")

score_map = counting_trees(map_of_trees)

scenic_max = 0
for row in score_map:
    print(row)
    scenic_max = max(scenic_max, max(row))
print(scenic_max)