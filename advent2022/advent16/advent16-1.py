from queue import Queue

def parse_line(line: str):
    
    valve   = line[6:8]
    flow    = int(line[23:].split(';')[0])
    tunnels = line.split(';')[1][23:].replace(' ', '').split(',')
    return valve, flow, tunnels


def best_flow(valves: dict[str, tuple[int, list[str]]], start_valve: str, time: int):
    Q = Queue()
    # set a dict with large distance to each valve and flow-rate
    calculated_flow = {k: [100, v[0]] for k, v in valves.items()}
    visited_valves = set()
    Q.put(start_valve)
    visited_valves.update({start_valve})
    while not Q.empty():
        valve = Q.get()
        if valve == start_valve:
            calculated_flow[valve][0] = 0
        for u in valves[valve][1]:
            if u not in visited_valves:
                # update the distance
                if calculated_flow[u][0] > calculated_flow[valve][0] + 1:
                    calculated_flow[u][0] = calculated_flow[valve][0] + 1

                Q.put(u)
                visited_valves.update({u})
    
    for key, value in calculated_flow.items():
        dist = value[0] + 1
        flow = value[1] * (time - dist) // dist ** 2
        calculated_flow[key] = [dist, flow]

    return calculated_flow

valves: dict[str, tuple[int,list[str]]] = {}

with open("./data_test.txt", 'r') as data:
    for line in data:
        valve = (parse_line(line[:-1]))
        valves[valve[0]] = list(valve[1:])

current_valve = 'AA'
time_remaining = 30
total_flow = 0
# while time_remaining > 0:
while time_remaining > 0:
    flows = sorted((best_flow(valves, current_valve, time_remaining)).items(), key=lambda x: x[1][1], reverse=True)
    print(flows)
    valve, time = flows[0]
    print(valve, time)
    if valves[valve][0] == 0:
        break
    time_remaining -= time[0]
    print(time_remaining)
    additional_flow = valves[valve][0] * time_remaining
    total_flow += additional_flow
    valves[valve][0] = 0
    current_valve = valve
    print("total flow:", total_flow)

print(total_flow)