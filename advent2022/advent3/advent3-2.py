from string import ascii_letters
from typing import Tuple, List

priority_list: List[str] = list(ascii_letters)

def priority_value (letter: str) -> int :
    return 1 + priority_list.index(letter)


total_priority: int = 0
with open("./data.txt", "r") as data:
    
    while True:
        sack_1: str = data.readline()[:-1]
        if sack_1 == "":
            break
        sack_2: str = data.readline()[:-1]
        sack_3: str = data.readline()[:-1]

        common_item: str = (set(sack_1) & set(sack_2) & set(sack_3)).pop()
        total_priority += priority_value(common_item)
        
print(total_priority)
