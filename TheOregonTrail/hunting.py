import random
import weather

class Hunt:
    def __init__(self):
        self.ammo = 0
        self.strength = 100
        self.food = 0
        self.chances = 80

    def add_ammo(self, amount): 
        self.ammo += amount
        print(f"You added {amount} ammo. Total ammo: {self.ammo}")

    def hunt(self):

        if self.ammo <= 0:
            print("You have no ammo! You can't hunt!")
            return

        print("You go out hunting")

        self.ammo -= random.randint(0, 10)
        success = random.choice([True, False])

        if success:
            found_food = random.randint(20, 200)
            carried_food = min(found_food, self.strength)
            self.food += carried_food

            print(f"You found {found_food} lbs of food, and carried back {carried_food} lbs.")
        else:
            print("You didn't find anything this time.")
        print(f"Ammo left: {self.ammo}, Total food: {self.food}")
        
