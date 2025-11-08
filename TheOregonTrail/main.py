from weather import Weather
from hunting import Hunt


def main():
    

    weather = Weather()
    hunt = Hunt()

    for _ in range(5):
        weather.next_day()
        print(weather.describe(), weather.get_modifiers())

    hunt.add_ammo(100)
    hunt.hunt()