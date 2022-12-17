from functools import cache
from time import perf_counter

def parse_line(line: str):
    valve   = line[6:8]
    flow    = int(line[23:].split(';')[0])
    tunnels = line.split(';')[1][23:].replace(' ', '').split(',')
    return valve, tunnels, flow

valves: dict[str, list[str]] = dict()
flows: dict[str, int] = dict()

with open("./data.txt", 'r') as data:
    for line in data:
        valve, tunnels, flow = (parse_line(line[:-1]))
        valves[valve] = tunnels
        flows[valve] = flow

# NOT Really my own solution sadly, but wanted to test out a solution
# I saw in C++ using but just using the cache decorator instead of doing it manually
@cache
def best_flow(current_valve: str, time_remaining: int, open: frozenset[str], elephant: bool) -> int:
    # if time runs out, return 0 (base case)
    if time_remaining == 0:
        if elephant:
            return best_flow('AA', 26, open, False)
        return 0

    # get the best flow for each valve connected to current valve
    flow_from_walking: int = 0
    for valve in valves[current_valve]:
        flow_from_walking = max(best_flow(valve, time_remaining-1, open, elephant), flow_from_walking)

    # if valve is not open and yieds a non-zero flow, then open and then continue 
    flow_from_opening: int = 0
    if current_valve not in open and flows[current_valve] > 0:
        tmp: set[str] = set(open)
        tmp.add(current_valve)
        flow_from_opening = flows[current_valve] * (time_remaining - 1) + best_flow(
            current_valve, time_remaining-1, frozenset(tmp), elephant)

    # return whatever is greater, opening and walking, or just walking
    return max(flow_from_walking, flow_from_opening)

starting_valve: str = 'AA'
starting_time: int = 26
elephant: bool = True
s = perf_counter()
total_flow = best_flow(starting_valve, starting_time, frozenset(), elephant)
print(total_flow)
print(perf_counter() - s)