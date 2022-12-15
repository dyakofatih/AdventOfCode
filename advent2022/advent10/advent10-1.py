
NOOP = 'noop'
ADDX = 'addx'

x_register = 1
clock = 0


strenghts= []

def calculate_signal_strenght(signal) :
    strenghts.append(x_register * signal)


def noop():
    return clock + 1

def addx(input):
    return x_register + input, clock + 2

with open("./data.txt", "r") as data:
    signals = [20, 60, 100, 140, 180, 220]
    

    for line in data:

        instruction = line[:-1].split(" ")

        if instruction[0] == NOOP:
            if clock % 40 == 19 and len(signals) != 0:
                clock = noop()
                calculate_signal_strenght(signals.pop(0))
            else:
                clock = noop()

        elif instruction[0] == ADDX:
            if clock % 40 == 18 and len(signals) != 0:
                calculate_signal_strenght(signals.pop(0))
                x_register, clock = addx(int(instruction[1]))
                

            elif clock % 40 == 19 and len(signals) != 0:
                calculate_signal_strenght(signals.pop(0))
                x_register, clock = addx(int(instruction[1]))

            else:
                x_register, clock = addx(int(instruction[1]))

    print(clock)
    print(x_register)
    print(strenghts)
    print(sum(strenghts))