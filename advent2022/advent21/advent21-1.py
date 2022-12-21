

from functools import cache
from time import perf_counter


monkeys = {}

with open('./data_test.txt', 'r') as data:

    for line in data:

        monkey, scream = line[:-1].split(':')
        # print(monkey, num_or_op)
        if scream.strip().isnumeric():
            monkeys[monkey] = int(scream)
        else:
            monkeys[monkey] = scream.split()


# @cache
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
sol = solve('root')
print(perf_counter() - s)
print(sol)
