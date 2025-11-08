from trail import trail_info
from main import main
def menu():
    print("""
    You may:
        1. Travel the trail
        2. Learn about the trail
        3. See the Oregon Top Ten
        4. Turn sound off
        5. Choose Management Options
        6. End
    """)

    try:
        option = int(input("What is your choice? "))
    except ValueError:
        print("Please enter a number between 1 and 6.")
        return

    if option == 1:
        input("Traveling the trail...")
        main()
    elif option == 2:
        trail_info()
    elif option == 3:
        print("Showing the Oregon Top Ten...")
    elif option == 4:
        print("Sound turned off.")
    elif option == 5:
        print("Opening Management Options...")
    elif option == 6:
        print("Ending program.")
    else:
        print("Invalid choice. Please select a number from 1 to 6.")