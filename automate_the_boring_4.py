import math, random, time


# Inventory Game

# Function that prints out Inventory list

def print_inventory (inventory):
    total_items = 0
    spacer = " "
    space_count = 3
    for item in inventory:
        
        space_count = space_count - len(str(inventory.get(item)))
        
        print(f"{inventory.get(item)} {spacer * space_count} {item}")
        
        total_items += inventory.get(item)

        space_count = 3

    print(f"Total Items = {total_items}")
    return total_items

# Function Test
# inventory_test1 = {"Rope": 3, "Potions": 45, "Ice_Blast": 1}
# print_inventory(inventory_test1)
