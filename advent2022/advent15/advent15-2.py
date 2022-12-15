
class Beacon:
    def __init__(self, x: int, y: int) -> None:
        self.x: int = x
        self.y: int = y


class Sensor:
    def __init__(self, x: int, y: int, bx: int, by: int) -> None:
        self.x: int = x
        self.y: int = y
        self.manhattan_radius: int = self.calc_distance(bx, by)

    def calc_distance(self, bx: int, by: int) -> int:
        return abs(
            self.x - bx) + abs(self.y - by)


def read_report_line(line: str) -> Sensor:

    line = line.replace(' ', '')
    _, line1, line2 = line.split('x')
    x, y = map(lambda n: int(n), line1[1:].split(
        ':')[0].replace('y=', '').split(','))
    bx, by = map(lambda n: int(n), line2[1:].replace('y=', '').split(','))

    sensor = Sensor(x, y, bx, by)
    return sensor


def sensor_reach_to_y(sensor: Sensor, y: int) -> set[tuple[int, int]]:

    
    x1 = abs(sensor.y - y) - sensor.manhattan_radius + sensor.x
    x2 = - abs(sensor.y - y) + sensor.manhattan_radius + sensor.x
    return [x1, x2]


def check_gap_at_y(y: int, limxy: int):
    intervals = list()
    for sensor in sensors:
        if sensor.manhattan_radius < abs(sensor.y - y):
            continue
        intervals.append(sensor_reach_to_y(sensor, y))
    intervals.sort()
    intervals[0][0] = 0
    intervals[-1][1] = limxy
    check_for_gap_in_intervals(intervals, y)


def check_for_gap_in_intervals(intervals: list[list[int, int]], y: int):
    
    stack = [intervals[0]]

    for i in intervals[1:]:
        if stack[-1][0] <= i[0] <= stack[-1][-1]:
            stack[-1][-1] = max(stack[-1][-1], i[-1])
        else:
            stack.append(i)
    
    if len(stack) > 1:
        for i1, i2 in zip(stack, stack[1:]):
            if i1[1] + 2 == i2[0]:
                print((i1[1] + 1) * 4_000_000 + y)
                # print(i1[1] + 1, y)
                exit(0)


sensors: list[Sensor] = list()
with open("./data.txt", 'r') as data:

    for line in data:
        sensor = read_report_line(line)
        sensors.append(sensor)

# the x and y max to check for
limxy = 4_000_000
####################
for y in range(limxy + 1):
    check_gap_at_y(y, limxy)