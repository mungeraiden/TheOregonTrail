import os
AMMO_FILE = "ammo.txt"

def read_ammo():
    with open(AMMO_FILE, "r") as f:
        return float(f.read())

def write_ammo(amount):
    with open(AMMO_FILE, "w") as f:
        f.write(str(amount))

