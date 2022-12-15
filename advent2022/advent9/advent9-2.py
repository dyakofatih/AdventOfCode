def move_head(head, direction):
    
    if direction == 'U':
        head[1] += 1
    elif direction == 'D':
        head[1] -= 1
    elif direction == 'R':
        head[0] += 1
    elif direction == 'L':
        head[0] -= 1

def simulate_tail(head, tail):

    # x and y axis difference
    x_d = head[0] - tail[0]     
    y_d = head[1] - tail[1]
    

    # close... no move 
    if abs(x_d) < 2 and abs(y_d) < 2 :
        ...

    # horizontal diff 2, vertical diff 1
    elif abs(x_d) == 2 and abs(y_d) == 1 :
        tail[1] = head[1]
        tail[0] = head[0] - 1 if x_d > 0 else head[0] + 1 
    
    # horizontal diff 1, vertical diff 2
    elif abs(x_d) == 1 and abs(y_d) == 2 :
        tail[0] = head[0]
        tail[1] = head[1] - 1 if y_d > 0 else head[1] + 1 

    # only horizontal diff
    elif abs(x_d) == 2 and abs(y_d) == 0 :
        tail[0] = head[0] - 1 if x_d > 0 else head[0] + 1

    # only vertical diff
    elif abs(x_d) == 0 and abs(y_d) == 2 :
        tail[1] = head[1] - 1 if y_d > 0 else head[1] + 1 

    # tail segment diff of 2 both horizontally and vertically
    elif abs(x_d) == 2 and abs(y_d) == 2 :
        tail[0] = head[0] - 1 if x_d > 0 else head[0] + 1
        tail[1] = head[1] - 1 if y_d > 0 else head[1] + 1 
    
    return (tail[0], tail[1])


with open("./data.txt", "r") as data:
    
    # starting point
    # head = [0, 0]   
    rope = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    visited = []

    for line in data:

        move = line[:-1].split(" ")
        direction = move[0]
        steps = int(move[1])

        
        for _ in range(steps):
            move_head(rope[0], direction)
            # print(head, end="")
            for i in range(1,9):
                simulate_tail(rope[i-1], rope[i])
            visited.append(simulate_tail(rope[8], rope[9]))
    
    # print("\n", visited)
    print(len(set(visited)))