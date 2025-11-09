FOOD_FILE = "food.txt"
import os

def read_food():
    with open(FOOD_FILE, "r") as f:
        return float(f.read())

# Write money to file
def write_food(amount):
    with open(FOOD_FILE, "w") as f:
        f.write(str(amount))
