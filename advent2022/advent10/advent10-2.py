
NOOP = 'noop'
ADDX = 'addx'

x_register: int = 1
clock: int = 0


def draw_pixel(sprite_pos: int, x_axis: int, new_row: bool) :
    
    pixel = '.'

    if x_axis >= sprite_pos and x_axis <= sprite_pos + 2:
        pixel = '#'

    if new_row:
        print("\n{}".format(pixel), end='')
    else:
        print(pixel, end='')



def addx(input):
    return x_register + input


with open("./data.txt", "r") as data :
  

    for line in data :

        instruction = line[:-1].split(" ")

        if instruction[0] == NOOP :
            draw_pixel(sprite_pos = x_register - 1, x_axis = clock % 40, new_row = clock % 40 == 0)
            clock += 1

        elif instruction[0] == ADDX :
            
            draw_pixel(sprite_pos = x_register - 1, x_axis = clock % 40, new_row = clock % 40 == 0)
            clock += 1
            draw_pixel(sprite_pos = x_register - 1, x_axis = clock % 40, new_row = clock % 40 == 0)
            clock += 1
            x_register = addx(int(instruction[1]))
                

