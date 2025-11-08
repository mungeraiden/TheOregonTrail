from weather import Weather
from hunting import Hunt
from shop import Shop
from party import Party
from clear import clear
from characterselection import CharecterSelection
from money import *
from randomevent import random_event

def main():
    
    character = CharecterSelection()
    character.set_up()

    party = Party()
    party.setup_party()

    shop = Shop()
    shop.money = read_money()
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

    input("Press ENTER to continue")
    clear()

    shop.store()
    clear()

    print("""
    Well then, you're ready
    to start. Good luck!
    You have a long and 
    difficult journey ahead
    of you.
    """)

    input("Press ENTER to continue")
    clear()
    

    
    miles_left = 2000
    
    weather = Weather()


    running = True
    while running:
        clear()
        if miles_left <= 0:
            running = False

        print("""
        You may:
            1. Continue on trail
            2. Check supplies
            3. Look at map
            4. Change pace
            5. Change food rations
            6. Stop to rest
            7. Buy supplies
        
        """)
        move = int(input("What is your choice? ")

        if move == 1:
            miles_left -= 300
            print(f"Miles to Oregon: {miles_left}")
            random_event()
        elif move == 2:

        elif move == 3:

        elif move == 4:

        elif move == 5:

        elif move == 6:

        else == 7:
