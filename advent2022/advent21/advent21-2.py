
from functools import cache
from time import perf_counter

monkeys = {}

with open('./data.txt', 'r') as data:

    for line in data:

        monkey, scream = line[:-1].split(':')
        # print(monkey, num_or_op)

        if scream.strip().isnumeric():
            monkeys[monkey] = int(scream)
        else:
            monkeys[monkey] = scream.split()


def solve(monkey: str):

    scream = monkeys[monkey]

    if isinstance(scream, int):
        return scream

    m1, op, m2 = scream

    if op == '+':
        return solve(m1) + solve(m2)
    elif op == '-':
        return solve(m1) - solve(m2)
    elif op == '*':
        return solve(m1) * solve(m2)
    else:
        return solve(m1) / solve(m2)


s = perf_counter()

m1, op, m2 = monkeys['root']

s2 = solve(m2)
print('s2:', s2)

val = 3_509_820_000_000
monkeys['humn'] = val
print(solve(m1)-s2)
s1 = 0
while int(s1) != int(s2):
    val -= 1
    monkeys['humn'] = val
    s1 = solve(m1)

print(val)
print(perf_counter() - s)
