from weather import Weather
from hunting import Hunt
from shop import Shop
from party import Party
from clear import clear
from characterselection import CharacterSelection
from money import read_money, write_money
from randomevent import random_event
from food import *
from ammo import *

def main():
    # --- Setup ---
    character = CharacterSelection()
    character.set_up()

    party = Party()
    party.setup_party()

    shop = Shop()
    shop.money = read_money()
    clear()

    input("Press ENTER to continue")
    clear()

    print("""
    It is 1848. Your jumping off 
    place for Oregon is Independence,
    Missouri. You must decide which
    month to leave Independence.
        1. March
        2. April
        3. May
        4. June
        5. July
    """)
    answer = int(input("What is your choice? "))

    clear()

    print(f"""
    Before leaving Independence you
    should buy equipment and 
    supplies. You have {shop.money} in
    cash, but you don't have to 
    spend it all now.
    """)

    input("Press ENTER to continue")
    clear()

    print("""
    You can buy whatever you need at
    Matt's General Store
    """)

    input("Press ENTER to continue")
    clear()

    print("""
    Hello, I'm Matt. So you're going
    to Oregon! I can fix you up with
    what you need:
        - a team of oxen to pull
        your wagon
        - clothing for both
        summer and winter
    """)

    input("Press ENTER to continue")
    clear()

    print("""
    Hello, I'm Matt. So you're going
    to Oregon! I can fix you up with
    what you need:
        - plenty of food for the 
        trip
        - ammunition for your
        rifles
        - spare parts for your wagon
    """)


    print(f"\nBefore leaving Independence you should buy equipment and supplies. You have ${shop.money}.")
    input("Press ENTER to continue")
    clear()

    shop.store()
    clear()

    print("\nWell then, you're ready to start. Good luck on your journey!")
    input("Press ENTER to continue")
    clear()

    miles_left = 2000
    weather = Weather()
    hunter = Hunt()
    running = True

    while running:
        clear()
        weather.next_day()
        print(f"Day {weather.day}, Weather: {weather.condition}, Temp: {weather.temperature}F")
        print(f"Miles to Oregon: {miles_left}")
        print(f"Party Health: {party.overall_health()}")
        print(f"Food: {shop.pounds_of_food} lbs, Ammo: {hunter.ammo}, Oxen: {shop.oxen}\n")

        print("""
        You may:
            1. Continue on trail
            2. Check supplies
            3. Look at map
            4. Change pace
            5. Change food rations
            6. Stop to rest
            7. Go hunting
            8. Buy supplies
        """)

        move = input("What is your choice? ")

        if move == "1":
            
            mods = weather.get_modifiers()
            miles_today = int(12 * mods["travel_modifier"])
            miles_left -= miles_today
            party.eat_food()
            print(f"You traveled {miles_today} miles today. Miles left: {miles_left}")

            event = random_event(party, shop, weather, character)
            print(f"Event: {event}")

        elif move == "2":
            print(f"Supplies:\nOxen: {shop.oxen}\nFood: {read_food()} lbs\nAmmo: {hunter.ammo}\nWagon Wheels: {shop.wagon_wheels}\nWagon Tongues: {shop.wagon_tongues}")
            input("Press ENTER to continue")
        elif move == "3":
            print(f"You are {2000 - miles_left} miles from Independence, {miles_left} miles to Oregon.")
            input("Press ENTER to continue")
        elif move == "4":
            print("Changing pace... (feature coming soon)")
            input("Press ENTER to continue")
        elif move == "5":
            print("""
                You can change the food rationing to the following:
                    1. Filling
                    2. Meager
                    3. Bare Bones            
            """)
            rationing = int(input("What is your choice? "))
            party.set_ration(rationing)

        elif move == "6":
            print("Stopping to rest...")
            party.rest()
            input("Press ENTER to continue")
        elif move == "7":
            hunter.hunt()
            input("Press ENTER to continue")
        elif move == "8":
            shop.store()
        else:
            print("Invalid choice.")

        if miles_left <= 0:
            print(r""" 
             __ __   ___   __ __      ___ ___   ____  ___      ___      ____  ______      ______   ___        ___   ____     ___   ____   ___   ____  
            |  |  | /   \ |  |  |    |   |   | /    ||   \    /  _]    |    ||      |    |      | /   \      /   \ |    \   /  _] /    | /   \ |    \ 
            |  |  ||     ||  |  |    | _   _ ||  o  ||    \  /  [_      |  | |      |    |      ||     |    |     ||  D  ) /  [_ |   __||     ||  _  |
            |  ~  ||  O  ||  |  |    |  \_/  ||     ||  D  ||    _]     |  | |_|  |_|    |_|  |_||  O  |    |  O  ||    / |    _]|  |  ||  O  ||  |  |
            |___, ||     ||  :  |    |   |   ||  _  ||     ||   [_      |  |   |  |        |  |  |     |    |     ||    \ |   [_ |  |_ ||     ||  |  |
            |     ||     ||     |    |   |   ||  |  ||     ||     |     |  |   |  |        |  |  |     |    |     ||  .  \|     ||     ||     ||  |  |
            |____/  \___/  \__,_|    |___|___||__|__||_____||_____|    |____|  |__|        |__|   \___/      \___/ |__|\_||_____||___,_| \___/ |__|__|
                                                                                                                                          
""")
            running = False
        elif party.is_dead():
            print(r"""
              ____   ____  ___ ___    ___       ___   __ __    ___  ____  
             /    | /    ||   |   |  /  _]     /   \ |  |  |  /  _]|    \ 
            |   __||  o  || _   _ | /  [_     |     ||  |  | /  [_ |  D  )
            |  |  ||     ||  \_/  ||    _]    |  O  ||  |  ||    _]|    / 
            |  |_ ||  _  ||   |   ||   [_     |     ||  :  ||   [_ |    \ 
            |     ||  |  ||   |   ||     |    |     | \   / |     ||  .  \
            |___,_||__|__||___|___||_____|     \___/   \_/  |_____||__|\_| 
            """)
            
            print(f"""
            You survived: {weather.day} days
            You traveled: {2000 - miles_left} miles
            """)

            running = False

        input("Press ENTER for next day")

