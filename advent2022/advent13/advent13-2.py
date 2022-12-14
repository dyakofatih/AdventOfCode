from functools import cmp_to_key


def check_order_recursive(list1, list2):

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
            return check_order_recursive(list1[1:], list2[1:])
    # both item are lists
    elif isinstance(list1[0], list) and isinstance(list2[0], list):
        res, done = check_order_recursive(list1[0], list2[0])
        if done:
            return res, True
        return check_order_recursive(list1[1:], list2[1:])
    # first item is an int, second is a list
    elif isinstance(list1[0], int) and isinstance(list2[0], list):
        res, done = check_order_recursive([list1[0]], list2[0])
        if done:
            return res, True
        return check_order_recursive(list1[1:], list2[1:])
    # first item is a list, second is an int
    elif isinstance(list1[0], list) and isinstance(list2[0], int):
        res, done = check_order_recursive(list1[0], [list2[0]])
        if done:
            return res, True
        return check_order_recursive(list1[1:], list2[1:])


def check_order(list1, list2):
    res, _ = check_order_recursive(list1, list2)
    return -1 if res else 1


with open('data_full.txt', 'r') as data:
    lists = [eval(l) for l in (line.strip() for line in data) if l]
lists.append([[2]])
lists.append([[6]])

lists.sort(key=cmp_to_key(check_order))
index_mul = 1
for i, line in enumerate(lists):
    if line == [[2]] or line == [[6]]:
        print(i+1)
        index_mul *= i+1
print(index_mul)
