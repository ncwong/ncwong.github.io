# Update this text to match your story.
start = '''
You wake up one morning and find that you aren't in your bed; you aren't even in your room.
You're in the middle of a giant room with two giant portals
A sign is hanging from the ivy: "You have one hour. Be wary of your choices."
'''

print(start)

print("Type 'left' to go left or 'right' to go right.") # Update to match your story.
user_input = input()
if user_input == "left":
    print("You decide to go to the left portal and suddenly, you are on a submarine") # Update to match your story.
    print("You make your way to the control room and you find three buttons, labeled 1, 6, and 7")
    print("The only clue that you can find is a calendar with today's date circled")
    print("Type in the button order below")
    user_input = input()
    if user_input == "716":
        print("A green light flashes and the submarine resurfaces above the water")
        print("After you've made it to the beach, you find two paths.")
        print("On the left is a cave and on the right is a path up a mountain.")
        print("Type 'left' to go left or 'right' to go right.") # Update to match your story.
        user_input = input()
        if user_input == "left":
            print("Once you've entered the cave, you trip on a wire which sets off a trap and you instantly die.")

        else:
            print("When you've reached the end of the trail, you find a portal and when you step through you're back in your room.")
            print("Congrats, you survived!")

    else:
        print("A red light flahses and everything goes dark. You've lost the game.")



    # Continue code to finish story.


elif user_input == "right":
    print("You choose to go right and you're on a spaceship!")
    print("You find a control panel and there are two buttons: up or down.")
    print("Type up to go up and down to go down.")
    user_input = input()
    if user_input == "up":
        print("You press the up button and the spaceship heads directly for the sun!")
        print("You end the last seconds of your life in a fiery blaze of terror.")
        print("You died.")

    else:
        print("You press the down the button and crash land on an unknown planet, miraculously survivng.")
        print("Upon hearing the impact, aliens emerge from seemingly nothing.")
        print("They immediately take you hostage to their lab base, and put you under a deep sleep.")
        print("In the end, the aliens kill you, using your body for human research.")
        print("Hey at least you died a hero. Somewhat.")
        # Update to match your story.

    # Continue code to finish story.
