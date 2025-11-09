from food import *

class Party:
    def __init__(self):
        self.members = [
            {"name": "Player", "health": 100},
            {"name": "Companion1", "health": 100},
            {"name": "Companion2", "health": 100},
            {"name": "Companion3", "health": 100}
        ]
        self.ration = 10
        self.food = read_food()

    def setup_party(self):
        print("Setting up your party members...")
        for i, member in enumerate(self.members[1:], start=1):
            name = input(f"Enter the name of companion {i}: ")
            member["name"] = name
        print("Party setup complete.\n")

    def set_ration(self, option):
        if option == 1:
            self.ration = 10
        elif option == 2:
            self.ration = 7
        else:
            self.ration = 5

    def eat_food(self):
        self.food = read_food()
        total_consumed = self.ration * len(self.members)
        self.food -= total_consumed

        if self.food < 0:
            self.food = 0
            self.reduce_health(25)
            total_consumed = 0
            print("You ran out of food! The party is starving.")
    
        write_food(self.food)
        print(f"The party ate {total_consumed} lbs of food. Food left: {self.food}")

    def overall_health(self):
        if not self.members:
            return 0
        return int(sum(member["health"] for member in self.members) / len(self.members))

    def reduce_health(self, amount):
        for member in self.members:
            member["health"] -= amount
            if member["health"] < 0:
                member["health"] = 0
        print(f"Party health reduced by {amount}.")

    def rest(self):
        # Resting restores some health
        for member in self.members:
            member["health"] += 10
            if member["health"] > 100:
                member["health"] = 100
        print("Party has rested. Health improved.")

    def remove_member(self):
        # Remove the member with the lowest health
        if self.members:
            dead_member = min(self.members, key=lambda m: m["health"])
            print(f"{dead_member['name']} has died.")
            self.members.remove(dead_member)

    def is_dead(self):
        self.members = [m for m in self.members if m["health"] > 0]
        return len(self.members) == 0
