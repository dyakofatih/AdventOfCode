
class Beacon:
    def __init__(self, x: int, y: int) -> None:
        self.x: int = x
        self.y: int = y


class Sensor:
    def __init__(self, x: int, y: int, beacon: Beacon) -> None:
        self.x: int = x
        self.y: int = y
        self.b: Beacon = beacon
        self.manhattan_radius: int = self.calc_distance()

    def calc_distance(self) -> int:
        return abs(
            self.x - self.b.x) + abs(self.y - self.b.y)


def read_report_line(line: str) -> tuple[Sensor, Beacon]:

    line = line.replace(' ', '')
    _, line1, line2 = line.split('x')
    x, y = map(lambda n: int(n), line1[1:].split(
        ':')[0].replace('y=', '').split(','))
    bx, by = map(lambda n: int(n), line2[1:].replace('y=', '').split(','))

    beacon = Beacon(bx, by)
    sensor = Sensor(x, y, beacon)

    return sensor, beacon


def sensor_reach_to_y(sensor: Sensor, y: int) -> set[tuple[int, int]]:

    coordinates: set[tuple[int, int]] = set()
    x1 = abs(sensor.y - y) - sensor.manhattan_radius + sensor.x
    x2 = - abs(sensor.y - y) + sensor.manhattan_radius + sensor.x
    return coordinates.union({(x1, y), (x2, y)})


sensors: list[Sensor] = list()
with open("./data.txt", 'r') as data:

    for line in data:
        sensor, _ = read_report_line(line)
        sensors.append(sensor)


coordinates: set[tuple[int, int]] = set()

# the y to check for
y = 2_000_000
####################
for sensor in sensors:
    if sensor.manhattan_radius < abs(sensor.y - y):
        continue
    coordinates.update(sensor_reach_to_y(sensor, y))


min_x, _ = min(coordinates, key=lambda x: x[0])
max_x, _ = max(coordinates, key=lambda x: x[0])

beacons_to_omit = set()
for sensor in sensors:
    if sensor.b.y == y:
        if sensor.b.x >= min_x or sensor.b.x <= max_x:
            beacons_to_omit.update(
                {(sensor.b.x, sensor.b.y)})


print("min_x:", min_x)
print("max_x:", max_x)
print("no. of beacons to omit:", len(beacons_to_omit))
print("total places where there cannot be any beacons = {}".format(
    max_x - min_x + 1 - len(beacons_to_omit)))
exit(0)
