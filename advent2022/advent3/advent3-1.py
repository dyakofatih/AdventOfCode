from string import ascii_letters
from typing import Tuple, List

priority_list: List[str] = list(ascii_letters)

def priority_value (letter: str) -> int :
    return 1 + priority_list.index(letter)

def get_compartments(list_of_items: str) ->  Tuple[str, str] :
    compartment_len: int = len(list_of_items) // 2
    return list_of_items[:compartment_len], list_of_items[compartment_len:]

total_priority: int = 0
with open("./data.txt", "r") as data:
    for sack in data.readlines():
        compartment_1, compartment_2 = get_compartments(sack[:-1])
        misplaced_item: str = (set(compartment_1) & set(compartment_2)).pop()
        total_priority += priority_value(misplaced_item)

print(total_priority)
