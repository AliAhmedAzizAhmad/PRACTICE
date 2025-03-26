#!/usr/bin/env python3

if __name__ == '__main__':
    user_input = int(input("How many eggs have you picked up this morning?"))
    box_12= user_input // 12
    remaining_eggs = user_input % 12

print(f"You will nedd {box_12} boxes of 12 eggs")
print(f"And you will have {remaining_eggs} left")

if remaining_eggs >= 6:
    box_6 = 1
    breakfast_eggs = remaining_eggs - 6
elif remaining_eggs < 6:
    box_6 = 0
    breakfast_eggs = remaining_eggs
if box_6:
    print("You will also need 1 box of 6 eggs")
else:
    print("You will not need a box of 6 eggs")
print(f"You will have {breakfast_eggs} left for your breakfast")