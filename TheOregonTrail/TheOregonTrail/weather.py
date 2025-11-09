import random
import hunting

class Weather:
    WEATHER_TYPES = {
        "Sunny": {"travel_modifier": 1.0, "health_modifier": 1.0},
        "Rainy": {"travel_modifier": 0.8, "health_modifier": 0.9},
        "Snowy": {"travel_modifier": 0.6, "health_modifier": 0.8},
        "Windy": {"travel_modifier": 0.9, "health_modifier": 0.95},
        "Stormy": {"travel_modifier": 0.5, "health_modifier": 0.85}
    }

    def __init__(self):
        self.condition = None
        self.temperature = None
        self.day = 0

    def generate_weather(self):
        self.condition = random.choice(list(self.WEATHER_TYPES.keys()))
        self.temperature = random.randint(30, 100)

    def next_day(self):
        self.day += 1
        self.generate_weather()

    def get_modifiers(self):
        mods = self.WEATHER_TYPES[self.condition].copy()

        if self.temperature < 40:
            mods["health_modifier"] *= 0.9
        elif self.temperature > 90:
            mods["health_modifier"] *= 0.95
        return mods

    def describe(self):
        return f"Day {self.day}: {self.condition}, {self.temperature}F"
