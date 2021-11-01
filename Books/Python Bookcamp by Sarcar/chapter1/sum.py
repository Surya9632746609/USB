# print("The sum of 12 and 5.7 are as follows:")
# print(12+5.7)
#
# print("The sum of 12 and 5.7 are as follows:", 12+5.7)



#


def welcome_user():
    """Transmit a Welcome Message."""
    print("Welcome to Learning Programming.")

welcome_user()

def animal_list(animal_kind, pet_name):
        """Display Details About Animal."""
        print(f "\nThis is a {animal_kind}.")
        print(f "My {animal_kind}’s name is {pet_name.title()}.")

animal_list ("Cat","Lucy")