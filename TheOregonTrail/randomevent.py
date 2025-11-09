import random

def random_event(party, shop, weather, character):

    luck = character.Character_Atributes[character.character]["Luck_modifier"]
    chance = random.randint(1, 100) * luck

    event_triggered = None

    #Broken Wagon
    if 21 <= chance <= 24:
        print("Oh no! Your wagon broke!")

        if shop.wagon_wheels > 0 or shop.wagon_tongues > 0:
            print("You have spare wagon parts to repair it.")
            choice = input("Do you want to use parts to repair it? (y/n) ").lower()
            if choice == "y":
                if shop.wagon_wheels > 0:
                    shop.wagon_wheels -= 1
                    print("You replaced a wagon wheel. Wagon repaired successfully!")
                elif shop.wagon_tongues > 0:
                    shop.wagon_tongues -= 1
                    print("You replaced the wagon tongue. Wagon repaired successfully!")
                event_triggered = "broken_wagon"
                return event_triggered

        print("You must attempt a manual repair without parts.")
        choice = input("Try to repair it yourself? (y/n) ").lower()
        if choice == "y":
            success = random.random() < character.Character_Atributes[character.character]["InstantRepair_modifier"]
            if success:
                print("You successfully repaired the wagon quickly!")
            else:
                print("Repair failed. You lost a day and some health.")
                party.reduce_health(5)
        else:
            print("You rest for a day while repairing the wagon slowly.")
            party.reduce_health(2)
        event_triggered = "broken_wagon"

    #Sickness
    elif 25 <= chance <= 29:
        print("Someone in your party got sick!")
        severity = random.randint(1, 3)
        party.reduce_health(severity * 5)
        print(f"The illness caused {severity * 5} health loss.")
        event_triggered = "sickness"

    #Robbery
    elif 30 <= chance <= 32:
        print("Bandits attacked and stole some of your supplies!")
        lost_food = min(shop.pounds_of_food, random.randint(10, 50))
        shop.pounds_of_food -= lost_food
        print(f"You lost {lost_food} lbs of food.")
        event_triggered = "robbery"

    #River Crossing Difficulty
    elif 33 <= chance <= 37:
        print("Crossing a river was difficult!")
        if weather.condition in ["Rainy", "Stormy"]:
            print("The river is especially dangerous due to the weather!")
            party.reduce_health(5)
        print("You lost some time traveling today.")
        event_triggered = "river_crossing"

    #Death
    elif 38 <= chance <= 39:

        print("Tragically, someone in your party has died.")
        party.remove_member()
        event_triggered = "death"

    #Oxen Die
    elif 40 <= chance <= 41:
        print("One of your oxen died!")
        if shop.oxen > 0:
            shop.oxen -= 1
        print(f"Oxen remaining: {shop.oxen}")
        event_triggered = "oxen_die"

    #Nothing / Lucky Event
    else:
        event_triggered = "nothing"
        # Small chance for a positive surprise
        if random.randint(1, 100) <= 5:
            bonus_food = random.randint(5, 25)
            shop.pounds_of_food += bonus_food
            print(f"Lucky day! You found {bonus_food} lbs of extra food.")

    return event_triggered
