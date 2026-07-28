# 21. Text Adventure Game
# Rooms:
# Forest
# River
# Village

# Player makes choices.
# Many endings.
# ======================

def start_game():

    choice = input("Choose a place (forest/river/village): ").lower()

    if choice == "forest":

        action = input("You see a treasure chest. Open or leave? ").lower()

        if action == "open":
            return "You found gold! You win!"
        else:
            return "You left the forest safely."


    elif choice == "river":

        action = input("A dangerous river blocks your way. Swim or boat? ").lower()

        if action == "swim":
            return "You crossed the river successfully!"
        else:
            return "You built a boat and survived safely."


    elif choice == "village":

        action = input("Talk to people or leave? ").lower()

        if action == "talk":
            return "The villagers gave you a hidden mission!"
        else:
            return "You ended your adventure."


    else:
        return "Unknown location."


print(start_game())