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
    
class HumanPlayer:
    def __init__(self, deck):
        self.__Deck = deck
    
    def getDeck(self):
        return self.__Deck

class ComputerPlayer:
    def __init__(self, deck):
        self.__Deck = deck
    
    def getDeck(self):
        return self.__Deck
        
class Game:
    def __init__(self):
        pass
        
    def PlayGame():
        pass

def generateDecks():
    numb = int(input("Enter the number of cards to be played: "))
    if numb < 4 or numb > 30 or numb%2 != 0:
        print("Number of cards in the deck has to be even and beween 4 to 30 cards. \n Returning to the menu...")
        Menu()
    
    FullDeck = []
    PlayerDeck = []
    ComputerDeck = []
    file = open("dogs.txt", "r")
    names = [x.replace("\n", "") for x in file.readlines()]
    for x in range(numb):
        FullDeck.append(createCard(names[x]))

    while FullDeck != []:
        PlayerDeck.append(FullDeck.pop(random.randrange(0,len(FullDeck))))
        ComputerDeck.append(FullDeck.pop(random.randrange(0,len(FullDeck))))
    
    return PlayerDeck, ComputerDeck

Game = Game()
def Menu():
    while True:
        choice = int(input("\nMenu:\n 1).Play Game \n 2).Quit \nChoice: "))
        if choice == 1:
            os.system('clear')
            PlayerDeck, ComputerDeck = generateDecks()
            HumanPlayer = HumanPlayer(PlayerDeck)
            ComputerPlayer = ComputerPlayer(ComputerDeck)
            Game.PlayGame()
        elif choice == 2:
            print("Thank you for playing.")
            os._exit()
        else:
            print("Invalid option.")

Menu()