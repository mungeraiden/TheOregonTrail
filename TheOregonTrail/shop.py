from money import *

class Shop:
    def __init__(self):
        self.oxen = 0
        self.sets_of_clothing = 0
        self.bullets = 0
        self.wagon_wheels = 0
        self.wagon_tongues = 0
        self.pounds_of_food = 0
        self.money = self

        self.prices = {
            "oxen": 40,               # per yoke (pair)
            "sets_of_clothing": 10,   # per set
            "bullets": 2,             # per box (20 bullets)
            "wagon_wheels": 15,
            "wagon_tongues": 12,
            "pounds_of_food": 0.20,   # per pound
        }

    def buy(self, item, quantity):
        if item not in self.prices:
            print("That item is not for sale.")
            return

        total_cost = self.prices[item] * quantity

        if total_cost > self.money:
            print("You don't have enough money!")
            return


        self.money -= total_cost
        setattr(self, item, getattr(self, item) + quantity)
        print(f"Bought {quantity} {item.replace('_', ' ')} for ${total_cost:.2f}. Remaining money: ${self.money:.2f}")

    def display_store(self):
        print("\nWelcome to the General Store!")
        print("Here is what you can buy: \n")
        print(f"1. Oxen (per yoke).............. ${self.prices['oxen']}")
        print(f"2. Sets of clothing............. ${self.prices['sets_of_clothing']}")
        print(f"3. Bullets (per box of 20)...... ${self.prices['bullets']}")
        print(f"4. Wagon wheels................. ${self.prices['wagon_wheels']}")
        print(f"5. Wagon tongues................ ${self.prices['wagon_tongues']}")
        print(f"6. Pounds of food............... ${self.prices['pounds_of_food']:.2f} per lb")
        print(f"\nYou have ${self.money} remaining.\n")

    def store(self):
        while True:
            self.display_store()
            choice = input("What would you like to buy? (1-6 or 'q' to quit): ").lower()

            if choice == 'q':
                if self.oxen >= 1:
                    print("Leaving the store...")
                    write_money(self.money)
                    break
                else:
                    print("You need Oxen to pull your Wagon!")

            items = [
                "oxen",
                "sets_of_clothing",
                "bullets",
                "wagon_wheels",
                "wagon_tongues",
                "pounds_of_food"
            ]

            if not choice.isdigit() or int(choice) not in range(1, 7):
                print("Invalid choice. Try again.")
                continue

            item = items[int(choice) - 1]
            try:
                quantity = float(input(f"How many {item.replace('_', ' ')} do you want to buy? "))
                self.buy(item, quantity)
            except ValueError:
                print("Please enter a valid number.")
