from money import *

class CharacterSelection:
    Character_Atributes = {
        "Banker": {"breakdown_modifier": .03, "InstantRepair_modifier": .6, "OxenInjuryMultiplier_modifier": 1, "RestingHealChance_modifier": .4, "Luck_modifier": 1},
        "Carpenter": {"breakdown_modifier": .015, "InstantRepair_modifier": .9, "OxenInjuryMultiplier_modifier": .9, "RestingHealChance_modifier": .5, "Luck_modifier": 2},
        "Farmer": {"breakdown_modifier": .0225, "InstantRepair_modifier": .75, "OxenInjuryMultiplier_modifier": .75, "RestingHealChance_modifier": .6, "Luck_modifier": 3}
    }
    def __init__(self):
        self.money = 400
        self.Health = "Healthy"
        self.Pace = "Steady"
        self.Rations = "Filling"
        self.PointMultiplier = 1
        self.character = None
        self.overall_health = 100
    def set_up(self):
        print("""
        Many kinds of people made the
        trip to Oregon.
    
        You may:
            1. Be a banker from Boston
            2. Be a carpenter from Ohio
            3. Be a farmer from Illinois
        """)

        characterChoice = int(input("What is your choice? "))

        if characterChoice == 1:
            self.character = "Banker"
            self.money += 1200

        elif characterChoice == 2:
            self.character = "Carpenter"
            self.money += 400
            self.PointMultiplier +=1

        elif characterChoice == 3:
            self.character = "Farmer"

        write_money(self.money)