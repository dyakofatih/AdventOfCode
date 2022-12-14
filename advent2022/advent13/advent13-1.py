

index_sum = 0
pair_index = 1


def check_order(list1, list2):

    # if only list2 is empty
    if len(list1) > 0 and len(list2) == 0:
        return False, True
    # if list1 is empty
    elif len(list1) == 0 and len(list2) > 0:
        return True, True
    elif len(list1) == 0 and len(list2) == 0:
        return True, False
    elif isinstance(list1[0], int) and isinstance(list2[0], int):
        if list1[0] > list2[0]:
            return False, True
        elif list1[0] < list2[0]:
            return True, True
        else:
            return check_order(list1[1:], list2[1:])
    # both item are lists
    elif isinstance(list1[0], list) and isinstance(list2[0], list):
        res, done = check_order(list1[0], list2[0])
        if done:
            return res, True
        return check_order(list1[1:], list2[1:])
    # first item is an int, second is a list
    elif isinstance(list1[0], int) and isinstance(list2[0], list):
        res, done = check_order([list1[0]], list2[0])
        if done:
            return res, True
        return check_order(list1[1:], list2[1:])
    # first item is a list, second is an int
    elif isinstance(list1[0], list) and isinstance(list2[0], int):
        res, done = check_order(list1[0], [list2[0]])
        if done:
            return res, True
        return check_order(list1[1:], list2[1:])


with open('data_full.txt', 'r') as data:

    for line in data:
        list1 = eval(line)
        # print(list1)
        list2 = eval(data.readline())
        # print(list2)
        _ = data.readline()

        in_order, _ = check_order(list1, list2)
        print("pair {} : {}".format(pair_index, in_order))
        index_sum += pair_index if in_order else 0
        pair_index += 1

print(index_sum)

""" list1 = [[1]]
list2 = [2]

print(check_order(list1, list2)) """
