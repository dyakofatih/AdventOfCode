from typing import List

class Monkey: 
    def __init__(self, monkey_id: int, 
                test_val: int, 
                target_monkeys: List[int], 
                starting_items: List[int], 
                operator: str, 
                operator_val: str):
        self.monkey_id: int = monkey_id
        self.test_val: int  = test_val
        self.target_monkeys: List[int]  = target_monkeys
        self.starting_items: List[int]  = starting_items
        self.operator: str      = operator
        self.operator_val: str  = operator_val
        self.no_of_inspections: int = 0


    def worry_level(self, item):
        # if the operation is +
        if self.operator == '+':
            if self.operator_val == 'old':
                return (item * 2) // 3
            else:
                return (item + int(self.operator_val)) // 3
        # if the operation is *
        else:
            if self.operator_val == 'old':
                return (item ** 2) // 3
            else:
                return (item * int(self.operator_val)) // 3

                
    def throw_item(self):
        self.no_of_inspections += 1
        item: int = self.starting_items.pop(0)
        item = self.worry_level(item)
        if item % self.test_val == 0:
            return item, self.target_monkeys[0]
        else:
            return item, self.target_monkeys[1]

    def catch_item(self, item: int):
        self.starting_items.append(item)
        
    
monkeys: List[Monkey] = []

with open("./data.txt", "r") as data:
        
    for i in range(8):

        monkey_id = int(data.readline()[-3])
        # print(monkey_id)

        items = [int(x) for x in data.readline()[:-1].replace(' ', '').split(':')[1].split(',')]
        # print(items)

        operation = data.readline()[:-1].split("= old")[1].split()
        operator = operation[0]
        operator_val = operation[1]
        # print(operator, operator_val)

        test_val = int(data.readline()[:-1].split()[-1])
        # print(test_val)

        monkey_true  = int(data.readline()[:-1].split()[-1])
        monkey_false = int(data.readline()[:-1].split()[-1])
        # print(monkey_true, monkey_false)
    
        data.readline()

        monkeys.append(Monkey(monkey_id=monkey_id, 
                                test_val=test_val,
                                target_monkeys=[monkey_true, monkey_false],
                                starting_items=items,
                                operator=operator,
                                operator_val=operator_val))

inspections = []

# for m in monkeys:
#     print(m.starting_items)
#     print(m.test_val)
#     print(m.operator, m.operator_val)
#     print(m.target_monkeys)

for i in range(20):

    for monkey in monkeys:

        for _ in range(len(monkey.starting_items)):
            thrown, monkey_id = monkey.throw_item()
            monkeys[monkey_id].catch_item(thrown)


for monkey in monkeys:
    inspections.append(monkey.no_of_inspections)
    print("Monkey", monkey.monkey_id, "inspected items", monkey.no_of_inspections, "times")

inspections.sort(reverse=True)
print("all the inspections", inspections)

print(inspections[0] * inspections[1])
