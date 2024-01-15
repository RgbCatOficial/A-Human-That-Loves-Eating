# Importing food (no food class yet) example: import Snack
from Snack import Snack
# Importing libs
import time

# not_over state is used to check if the user already ate the food successfully or not and manages how the main loop works
not_over = True

# Creating food variables (currently, there is no food class) example: snack = Snack(). Also, please make the classes with the first letter highCap and the variables all lowcap
snack = Snack()
# List containing all food exported (please add the food variable here)
food = [snack]

# List to add all names
food_names = []

# Catching all food names
for food_item in food:
    food_names.append(food_item.name)

# Starting main loop
while not_over:
    # Showing the options
    print("Current available food in the table:\n----------------------------------------")

    # Loop to show all the food currently exported from the classes: (there is no food yet, so there is a loop that only runs if there is something in "food")
    if not len(food) == 0:
        for food_item in food:
            time.sleep(1)
            print(food_item.name)
    else:
        print("There is no food currently. ")

    # Here is possible to eat a food and see what happens! (There is no food yet so whatever)
    user_request = input("What do you want to eat (Type '!!!' to see the food options again and Ctrl+C to leave)? ")

    # If the user types "!!!", it will display the options again, using a {continue}
    if user_request == "!!!":
        print("So you want to see the options again, don't you? ")
        continue  # Go back to the loop start and ignore all the following steps

    # This loop verifies which food the user wants to eat. In case the food does not exist in the list, the user is requested again with an error message.
    while True:
        # If user request is actually somewhere in the list, it is time to check which is the food that they want to eat.
        if user_request in food_names:
            # Nom nom nom is a sound effect of eating something, and there are some points that give extra suspense for the user. After this, the class method is activated.
            print("Nom Nom Nom")
            for _ in range(0, 2):
                time.sleep(1)
                print(".")
            # Use the item directly from the loop instead of using an index
            for food_item in food:
                if user_request == food_item.name:
                    food_item.eat()
            print("Enjoyed the meal? What about eating something else! Run the code again and check for more food. ")
            not_over = False
            break  # After the user eats, he is requested to run the code again to experience something else. This breaks the loop and stops the code.
        else:
            user_request = input("It looks like the food you typed doesn't exist in this program. Please try again or see the options again typing '!!!'. ")
            if user_request == "!!!":
                break
