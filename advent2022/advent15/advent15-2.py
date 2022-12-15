
import functools


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


def reach_none(x: int, y: int) -> bool:
    bools: list[bool] = [True for _ in range(len(sensors))]
    for i, sensor in enumerate(sensors):
        bools[i] = abs(sensor.x - x) + abs(sensor.y - y) <= sensor.manhattan_radius
    return any(bools)


    

sensors: list[Sensor] = list()
with open("./data_test.txt", 'r') as data:

    for line in data:
        sensor = read_report_line(line)
        sensors.append(sensor)

sensors.sort(key=lambda s: s.x)

# the y to check for
xylim = 20
####################

for x in range(xylim + 1):
    if x % 100 == 0:
        print(x)
    for y in range(xylim + 1):

        if not reach_none(x, y):
            print(x * 4_000_000 + y)
            exit()