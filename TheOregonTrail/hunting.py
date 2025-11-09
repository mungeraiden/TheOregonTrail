import random
from food import read_food, write_food
from ammo import read_ammo, write_ammo

class Hunt:
    def __init__(self):
        self.ammo = read_ammo()
        self.food = read_food()
        self.strength = 100
        self.base_chances = 80

    def add_ammo(self, amount):
        if amount <= 0:
            print("You must add a positive amount of ammo.")
            return

        self.ammo += amount
        print(f"You added {amount} ammo. Total ammo: {self.ammo}")
        write_ammo(self.ammo)

    def hunt(self):
        if self.ammo <= 0:
            print("You have no ammo! You can't hunt!")
            return

        print("You go out hunting...")

        ammo_used = random.randint(1, min(10, self.ammo))
        self.ammo -= ammo_used

        success_chance = min(95, self.base_chances + self.ammo // 10)
        success = random.randint(1, 100) <= success_chance

        if success:

            found_food = random.randint(20, 200)
            carried_food = min(found_food, self.strength)
            self.food += carried_food
            print(f"Success! You found {found_food} lbs of food and carried back {carried_food} lbs.")
        else:
            print("You didn't find anything this time.")

        print(f"Ammo used: {ammo_used}, Ammo left: {self.ammo}, Total food: {self.food}")

        write_food(self.food)
        write_ammo(self.ammo)

    def status(self):
        print(f"Ammo: {self.ammo}, Food: {self.food}, Strength: {self.strength}")
