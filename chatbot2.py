# --- Define your functions below! ---
def intro():
    print(" 🤖 Hello, I am CHATBORT 🤖")
    print("🤖 Let's talk! 🤖")
    print("🤖 [instructions for use] 🤖")

#   Rock paper scissors
#different bort personalities

def choosePersonality():
    print("Choose a personality to talk to. You can choose:")
    choice = input("Mean, Nice, or Nervous ")
    return choice


#def process_input(answer):
    if answer == "Hi":
        print("Greetings from CHATBORT")
    else:
        print("That's cool!")
    #Do processing input stuff

# --- Put your main program below! ---
def main():

    mean = {"Hi" : "🤖 CAN YOU LEAVE??? 🤖", "What's up?" : "🤖 DON'T SPEAK TO ME, FOOL! 🤖",
            "How are you?" : "🤖 TERRIBLE, NOW THAT I'M TALKING TO YOU... 🤖"}

    nice = {"Hi" : "🤖 HI, IT'S SO NICE TO MEET YOU! 🤖",
            "What's up?" : "🤖 OH, I'M JUST TALKING TO THE MOST INTERESTING PERSON! 🤖",
            "How are you?" : "🤖 OH, I'M JUST LOVELY! 🤖"}

    nervous = {"Hi" : "🤖", "What's up?" : "🤖 ...UM, HI 🤖", "How are you?" : "🤖 NERVOUS! 🤖"}

    userChoice = choosePersonality()


    intro()

    while True:
        answer = input("(What will you say?) ")

        if userChoice == "Mean":
            if answer in mean:
                print(mean[answer])
            else: print("🤖 I DON'T UNDERSTAND YOUR GIBBERSIH, SWINE. 🤖")
        elif userChoice == "Nice":
            if answer in nice:
                print(nice[answer])
            else: print("🤖 TERRIBLY SORRY, BUT I DON'T UNDERSTAND 🤖")
        elif userChoice == "Nervous":
            if answer in nervous:
                print(nervous[answer])
            else: print("🤖 THE WORLD IS LARGE AND CONFUSING AND I AM SMALL AND SCARED 🤖")



# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
