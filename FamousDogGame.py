import random, os

def createCard(name):
    Data = {
        "Name" : name,
        "Exercise" : random.randint(1,5),
        "Intelligence" : random.randint(1,100),
        "Friendliness" : random.randint(1,10),
        "Drool" : random.randint(1,10)    
        }
    return Data
    
def Menu():
    while True:
        try:
            choice = int(input("\nMenu:\n 1).Play Game \n 2).Quit \nChoice: "))
        except: print("Input is not an interger.") 
        if choice == 1:
            os.system('clear')
            PlayGame()
        elif choice == 2:
            print("Thank you for playing.")
            os._exit()
        else:
            print("Invalid option.")
            
def generateDecks():
    FullDeck = []
    try:
        numb = int(input("Enter the number of cards to be played: "))
    except: print("Input is not a interger. \n Returning to the menu...", Menu())

    if numb < 4 or numb > 30 or numb%2 != 0:
        print("Number of cards in the deck has to be even and beween 4 to 30 cards. \n Returning to the menu...")
        Menu()
        
    file = open("dogs.txt", "r")
    names = [x.replace("\n", "") for x in file.readlines()]
    
    for x in range(numb):
        FullDeck.append(createCard(names[x]))

    PlayerDeck = []
    ComputerDeck = []
    while FullDeck != []:
        PlayerDeck.append(FullDeck.pop(random.randrange(0,len(FullDeck))))
        ComputerDeck.append(FullDeck.pop(random.randrange(0,len(FullDeck))))
    
    return PlayerDeck, ComputerDeck

def displayCard(card):
    print("\n-------------------------------------")
    for key, value in card.items():
        print(key,"  --  ",value)
    print("-------------------------------------\n")
    
def chooseCategory():
    while True:
        try:
            Choice = int(input("Choose a category: \n 1).Exercise \n 2).Intelligence \n 3).Friendliness \n 4).Drool \nChoice: "))
            if Choice >= 1 and Choice <= 4:
                return Choice
            else:
                print("Invalid option. Please try again.")
        except: print("Invalid option. Please try again.")

def PlayGame():
    PlayerDeck, ComputerDeck = generateDecks()
    decks = [PlayerDeck, ComputerDeck]
    DataHolder = [None, None]
    winner = "Player"
    while PlayerDeck != [] and ComputerDeck != []:
        if winner == "Player":
            print("\nYour Card")
            displayCard(PlayerDeck[0])
            Choice = chooseCategory()
        elif winner == "Computer":
            print("\nOpponent's Card")
            displayCard(ComputerDeck[0])
            Choice = random.randint(1,4)
        
        for index, deck in enumerate(decks):
            if Choice == 1:
                DataHolder[index] = (deck[0]["Exercise"],"E")
            elif Choice == 2:
                DataHolder[index] = (deck[0]["Intelligence"],"I")
            elif Choice == 3:
                DataHolder[index] = (deck[0]["Friendliness"],"F")
            elif Choice == 4:
                DataHolder[index] = (deck[0]["Drool"],"D")
        
        if DataHolder[0][1] == "D":
            if DataHolder[0][0] <= DataHolder[1][0]:
                winner = "Player"
            else:
                winner = "Computer"
        else:
            if DataHolder[0][0] >= DataHolder[1][0]:
                winner = "Player"
            else:
                winner = "Computer"

        if winner == "Player":
            print("Player wins this round!")
            PlayerDeck.append(ComputerDeck.pop(0))
            PlayerDeck.append(PlayerDeck.pop(0))
        else:
            print("Computer wins this round!")
            ComputerDeck.append(PlayerDeck.pop(0))
            ComputerDeck.append(ComputerDeck.pop(0))

        nextRound = input("Press ENTER to proceed to the next round")
        os.system("clear")

    print(f"{winner}, is the winner of this match. Returning to the menu...")
    Menu()

Menu()


