MONEY_FILE = "money.txt"
import os

def read_money():
    with open(MONEY_FILE, "r") as f:
        return float(f.read())

# Write money to file
def write_money(amount):
    with open(MONEY_FILE, "w") as f:
        f.write(str(amount))
