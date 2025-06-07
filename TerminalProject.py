# Welcome to my mystery murder game! The game is set in the late 1800's 
# The game consist of a series of multiple choice questions each opening a 
# different storyline trajectory.


# Starting the game with a while loop so the player can exit or restart the game 
# once the game is finished or exits mid game due to a crossroads.
play_again = "yes"
while play_again.lower() == "yes":
# Prologue setting the scene of the game    
    print("Welcome to the case of the Ashwood Mystery! \n"
    "You play Inspector Elias Wren, a brilliant but underappreciated detective with \n"
    "a reputation for solving cases the Yard can’t. A wealthy industrialist, \n"
    "Lord Ashwood, is found dead in his locked study — suicide, says the official \n"
    "report. But you receive a mysterious letter signed “A Witness,” claiming... \n"
    "IT WAS MURDER!"
    "\n")
    print("You sit alone in your candlelit flat when a knock disturbs the silence. \n"
    "No visitor — just an envelope slipped under the door. It reads: \n"
    "\n"
    "The death of Lord Ashwood was no suicide. I saw what happened. If you value \n"
    "truth, begin with the family.")
# Step 1 is the first question in the game that opens up possible outcomes
    step1 = (int(input("What do you do? \n"
    "1. Go to Ashwood Manor immediately \n"
    "2. Inform Inspector Mallory at Scotland Yard \n"
    "3. Burn the letter and forget it \n"
    "")))
    print("\n")
# The if loop creats options and outcomes for the first scenario 
    if step1 == 1:
        print("You arrive at the estate. Lord Ashwood was found with a pistol in \n"
        "his hand, door locked from the inside. You notice: \n"
        "* A spilled brandy glass \n"
        "* A torn photograph \n"
        "* Scorch marks on the desk")
    elif step1 == 2:
        print("Just say you are boring!") # Will end the game
    else:
        print("GAME OVER!") # This will end the game
    print("\n")
# Step 1 is the first question in the game that opens up possible outcomes
    step2 = int(input("Where do you investigate first? \n"
    "1. Examine the pistol and the scorch marks \n"
    "2. Ask Miss Violet Ashwood about the torn photo \n"
    "3. Look for fingerprints or signs of intrusion \n"
    ""))
    print("\n")
    if step2 == 1:
        print("You notice the burn is from chemicals, not gunpowder. \n"
            "*Clue unlocked: Acid damage — possibly sabotage*")
    elif step2 == 2:
        print("Violet claims the photo was of her mother — whom her father banished. \n"
            "*Clue unlocked: Emotional, evasive. Suspicious.*")
    else:
        print("No fingerprints found! \n"
            "*Clue unlocked: No sign of forced entry. The killer was inside.*")
    print("\n")
    print("You notice the tab of a card sticking out of MR. Ashwood's \n"
        "pocket. A secret members card to the 'The Veiled Concord' \n"
        "* The Veiled Concord is a secret society of the elite. \n"
        "* The card is stained with blood. \n"
        "\n"
        "You have a hunch that the society is involved in his murder. \n"
        "\n"
        "Enter the Veiled Concord in London but to enter you must \n"
        "solve the riddle! \n")
    print("The hour is late, the veil is thin \n"
        "To enter, solve what lies within! \n" 
        "Times the number of point on a compass rose by the number of letters in \n" 
        "the title of this club")
# Adding some contro variables to get more user input 
    compass = int(input("How many points on a compass rose? ")) 
    title = int(input("How many letters in the title of the club? "))

    if compass == 8 and title == 16:
        print("ACCESS GRANTED!")
    else:
        print("Try again!")
    print("\n")
    print("To speak to the owner of the club you need to win at the dice game! \n"
        "This is a game of chance and requires you to roll a 6 \n"
        "You have 3 chances to roll the dice before you are kicked out! \n"
        "Good Luck!"
        "\n")

# The user is prompted to roll the dice and if they roll a 6 they can proceed
# If they do not roll a 6 they are prompted to try again
# If they fail to roll a 6 after 3 attempts they are kicked out of the club (game over)
    import random

    for attempt in range(3):
        input("Press Enter to roll the dice...")  # Simulates user rolling the dice
        dice1 = random.randint(1, 6) # Generates a random number between 1 and 6
        print(f"You rolled a {dice1}.") # Displays the result of the roll

        if dice1 == 6:
            print("You may proceed!")
            break
        else:
            print("Try again!") # If the user does not roll a 6, they are prompted to try again

    else:
        print("No more tries left. Access denied game over!.")
# The else statement is executed if the for loop completes without a break
# The user is prompted to try again and if they fail 3 times they are kicked out of the club

# If the user rolls a 6 they are allowed to enter the club and are greeted by the owner
    print("\n")
    print("You enter the club and are greeted by the owner, while you are waiting \n"
            "for your drink you overhear a conversation saying that the \n"
            "Lord Ashwood was a member of the club and was involved in a secret \n"
            "deal with the owner. \n"
            "'Ashwood was going to sell the prototype to the French. He got greedy'.\n")
    print("\n")
    print("Out the corner of your eye you see the club owner's office \n"
        "You can either: \n"
        "1. Confront the owner about the deal \n"
        "2. Sneak into the club owners office \n"
        "3. Call Inspector Mallory and inform him about the deal \n")
# The user is prompted to make a choice and the game continues based on their choice
    step3 = int(input("What do you do? "))
    print("\n")
    if step3 == 1:
        print("The owner denies everything and throws you out of the club. \n"
            "GAME OVER!")
    elif step3 == 2:
        print("You sneak into the club owner's office \n"
            "You see a letter on the desk with the same handwriting as the letter \n"
            "you received. \n"
            "It reads: \n"
            "'The deal is done. Ashwood is dead. The prototype is ours.' \n"
            "You take the letter and leave the office. \n"
            "You are now back at Ashwood Manor.")
        print("\n ")
        print("YOU SOLVED THE CASE! \n")
    elif step3 == 3:
        print("You call Inspector Mallory and inform him about the deal. \n"
            "He tells says he will take if from here and that you should go home. \n"
            "GAME OVER!")
    else:
        print("Invalid choice. Please try again.")
    print("\n") 
    print("Thank you for playing the Ashwood Mystery! \n"
        "You have solved the case and brought the killer to justice. \n"
        "Until next time, Inspector Wren!")
    print("\n")
# The user is prompted to play again or exit the game
play_again = input("Would you like to play again? (yes/no): ")
print("\n")
if play_again.lower() == "yes":
    print("Restarting the game...")
elif play_again.lower() == "no":
    print("Thank you for playing!")
else:
    print("Invalid input. Please enter 'yes' or 'no'.")
# The game will end here if the user chooses not to play again.
