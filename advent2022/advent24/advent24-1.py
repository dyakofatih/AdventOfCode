from time import perf_counter


# s = perf_counter()
# sum1 = 0
# for i in range(1_000_000_00):
#     sum1 += i
# print(sum1)
# print(perf_counter() - s)

calc_to = 1_000_000_000
s = perf_counter()
sum2 = sum(range(calc_to))
print(int(sum2))
print(perf_counter() - s)
