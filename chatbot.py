class Personality():
    hiResponse = ""
    whatsUpResponse = ""
    howAreYouResponse = ""
    otherResponse = ""

    def processInput(self, response):
        if response == "Hi":
            print(self.hiResponse)
        elif response == "What's up?":
            print(self.whatsUpResponse)
        elif response == "How are you?":
            print(self.howAreYouResponse)
        else:
            print(self.otherResponse)

# --- Define your functions below! ---
def intro():
    print(" 🤖 Hello, I am CHATBORT 🤖")
    print("🤖 Let's talk! 🤖")
    print("🤖 [instructions for use] 🤖")

#   Rock paper scissors
#different bort personalities

def choosePersonality():
    print("Choose a personality to talk to. You can choose:")
    choice = input("Mean, Nice, or Nervous")
    return choice

def process_input(response):
    if response == "Hi":
        print("GREEtINGS FROM CHATBORT")
    else:
        print("THAT'S COOL! ")

#def process_input(answer):
    if answer == "Hi":
        print("Greetings from CHATBORT")
    else:
        print("That's cool!")
    #Do processing input stuff

# --- Put your main program below! ---
def main():
    userChoice = choosePersonality()
    print(userChoice)
    niceRobot = Personality()
    niceRobot.hiResponse = "🤖 HI, IT'S So NICE TO MEET YOU! 🤖"
    niceRobot.whatsUpResponse = "🤖 OH, I'M JUST TALKING TO THE MOST INTERESTING PERSON! 🤖"
    niceRobot.howAreYouResponse = "🤖 OH, I'M JUST LOVELY! 🤖"
    niceRobot.otherResponse = "🤖 TERRIBLY SORRY, BUT I DON'T UNDERSTAND 🤖"

    meanRobot = Personality()
    meanRobot.hiResponse = "🤖 CAN YOU LEAVE?? 🤖"
    meanRobot.whatsUpResponse = "🤖 DON'T SPEAK TO ME, FOOL! 🤖"
    meanRobot.howAreYouResponse = "🤖 TERRIBLE, NOW THAT I'M TALKING TO YOU. 🤖"
    meanRobot.otherResponse = "🤖 I DON'T UNDERSTAND YOUR GIBBERSIH, SWINE. 🤖"

    nervousRobot = Personality()
    nervousRobot.hiResponse = "🤖"
    nervousRobot.whatsUpResponse = "🤖 ...UM, HI 🤖"
    nervousRobot.howAreYouResponse = "🤖 NERVOUS! 🤖"
    nervousRobot.otherResponse = "🤖 THE WORLD IS LARGE AND CONFUSING AND I AM SMALL AND SCARED 🤖"

    intro()

    while True:
        answer = input("(What will you say?) ")

        if (userChoice == "Nice"):
            niceRobot.processInput(answer)
        elif (userChoice == "Mean"):
            meanRobot.processInput(answer)
        elif (userChoice == "Nervous"):
            nervousRobot.processInput(answer)


# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
