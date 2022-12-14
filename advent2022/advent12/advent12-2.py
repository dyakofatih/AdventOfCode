import string


class QItem:
    def __init__(self, row, col, dist):
        self.row = row
        self.col = col
        self.dist = dist

    def __repr__(self):
        return f"QItem({self.row}, {self.col}, {self.dist})"


def minDistance(grid, start_item):
    source = start_item

    # To maintain location visit status
    visited = [[False for _ in range(len(grid[0]))]
               for _ in range(len(grid))]
    # applying BFS on matrix cells starting from source
    queue = []
    queue.append(source)
    visited[source.row][source.col] = True
    while len(queue) != 0:
        source = queue.pop(0)

        # Destination found;
        if (grid[source.row][source.col] == 'E'):
            return source.dist

        # moving up
        if isValid(source.row - 1, source.col, grid, visited,
                   grid[source.row][source.col]):
            queue.append(QItem(source.row - 1, source.col, source.dist + 1))
            visited[source.row - 1][source.col] = True

        # moving down
        if isValid(source.row + 1, source.col, grid, visited,
                   grid[source.row][source.col]):
            queue.append(QItem(source.row + 1, source.col, source.dist + 1))
            visited[source.row + 1][source.col] = True

        # moving left
        if isValid(source.row, source.col - 1, grid, visited,
                   grid[source.row][source.col]):
            queue.append(QItem(source.row, source.col - 1, source.dist + 1))
            visited[source.row][source.col - 1] = True

        # moving right
        if isValid(source.row, source.col + 1, grid, visited,
                   grid[source.row][source.col]):
            queue.append(QItem(source.row, source.col + 1, source.dist + 1))
            visited[source.row][source.col + 1] = True

    return -1


alfa = list(string.ascii_lowercase)
heights = {}
for i, char in enumerate(alfa):
    heights[char] = i
heights['S'] = 0
heights['E'] = 25
# checking where move is valid or not


def isValid(x, y, grid, visited, prev):
    if x < 0 or y < 0:
        return False
    elif x >= len(grid) or y >= len(grid[0]):
        return False
    elif visited[x][y]:
        return False
    elif heights[grid[x][y]] - heights[prev] <= 1:
        return True
    else:
        return False


with open("./data.txt", "r") as data:

    height_map = [[x for x in line[:-1]] for line in data]


# Finding the source to start from
shortest_path = 100000
for row in range(len(height_map)):
    for col in range(len(height_map[row])):
        if height_map[row][col] == 'S' or height_map[row][col] == 'a':
            distance = minDistance(height_map, QItem(row, col, 0))
            if distance != -1:
                if distance < shortest_path:
                    shortest_path = distance
                    print("new shortest path:", shortest_path)

""" for row in height_map:
    print(row) """
print("shortest path:", shortest_path)
