codes_dict = {}
codes_list = []

########
mul = 811589153
########

with open('./data.txt', 'r') as data:
    for i, line in enumerate(data):
        codes_list.append(int(line) * mul)
        codes_dict[i] = [i, int(line) * mul]

# print(codes_dict)
# print(codes_list)
mod_len = len(codes_list)
# print(codes_list)
for _ in range(10):
    for i in range(mod_len):
        idx, val = codes_dict[i]
        if val == 0:
            continue
        new_idx = (idx+val) % (mod_len - 1)

        if new_idx == 0:
            new_idx = mod_len - 1
        codes_list.pop(idx)
        codes_list.insert(new_idx, val)

        if new_idx > idx:
            codes_dict = {k: [v[0]-1 if idx < v[0] <=
                              new_idx else v[0], v[1]] for k, v in codes_dict.items()}
        elif new_idx < idx:
            codes_dict = {k: [v[0]+1 if new_idx <= v[0] <
                              idx else v[0], v[1]] for k, v in codes_dict.items()}
        codes_dict[i] = [new_idx, val]

    # print(codes_list)
    # print(codes_dict, '\n')


zero1k = codes_list[(codes_list.index(0) + 1000) % mod_len]
zero2k = codes_list[(codes_list.index(0) + 2000) % mod_len]
zero3k = codes_list[(codes_list.index(0) + 3000) % mod_len]

print(zero1k + zero2k + zero3k)
