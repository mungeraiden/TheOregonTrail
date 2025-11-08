class Party:
    def __init__(self):
        self.leader = ""
        self.passengers = []

    def setup_party(self):
        print("Welcome to The Oregon Trail!\n")
        self.leader = input("What is the first name of the wagon leader? ")

        print("\nNow enter the first names of the other members of your party.")
        for i in range(1, 5):
            name = input(f"Member #{i}: ")
            self.passengers.append(name)

        print("\nYour party is ready to go!")
        print(f"Leader: {self.leader}")
        print(f"Traveling companions: {', '.join(self.passengers)}")



