import random

def random_event():
    chance = random.randint(1, 100)
    
    # Broken wagon (4% chance)
    if 21 <= chance <= 24:
        print("Oh no! Your wagon broke! You have to stop and fix it.")
        return "broken_wagon"
    
    # Sickness (5% chance)
    elif 25 <= chance <= 29:
        print("Someone in your party got sick. You need to rest!")
        return "sickness"
    
    # Robbery (3% chance)
    elif 30 <= chance <= 32:
        print("Bandits attacked and stole some of your supplies!")
        return "robbery"
    
    # River crossing difficulty (5% chance)
    elif 33 <= chance <= 37:
        print("Crossing a river was difficult! You lost some time.")
        return "river_crossing"
    
    # Death (2% chance)
    elif 38 <= chance <= 39:
        print("Tragically, someone in your party has died.")
        return "death"
    
    # Oxen die (2% chance)
    elif 40 <= chance <= 41:
        print("One of your oxen died! Your wagon is slower now.")
        return "oxen_die"
    
    # Nothing happens (rest of the time)
    else:
        # normal day, nothing happens
        return "nothing"
