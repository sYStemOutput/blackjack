from random import choice
import time

def fillUpCards():
    d = list()
    
    # Fills up list 'd'
    for j in range(4):    
        for i in range(1, 10):
            d.append(i)
        d.append(10), d.append(10), d.append(10), d.append(10)    
                
    return d

def starterDeck(userCards, deck):
    card_one = choice(deck)
    deck.remove(card_one)
    card_two = choice(deck)
    deck.remove(card_two)
    
    userCards.append(card_one)
    userCards.append(card_two)
    
    return userCards, deck

def hit(deck):
    c = choice(deck)
    deck.remove(c)
    return c, deck

def checkSums(userCards, playerTurn, isWin):
    sumOne, sumTwo = 0, 0
    
    for i in userCards:
        if i == 1:
            sumOne += 1
            sumTwo += 11
        else:
            sumOne += i
            sumTwo += i
    
    user = ""
    if playerTurn:
        user = "Player"
    else:
        user = "CPU"    
        
    """ if sumOne == sumTwo:
        print(user + "'s sum: " + str(sumOne) + "\n")
    else:
        print(user + "'s sum: " + str(sumOne) + " or " + str(sumTwo) + "\n") """
        
    if sumOne == 21 or sumTwo == 21:
        print("Blackjack! The " + user + " wins!")
        return True
    elif sumOne > 21 and sumTwo > 21:
        print("Bust! The " + user + " has lost!")
        return True
        
def printCardsList(cards):
    
    print("[SUM: " + str(sum(cards)) + "]")
    
    print("+=====+ " * len(cards))
    print("|\   /| " * len(cards))
    print("| \ / | " * len(cards))
    for card_num in cards:
        if card_num == 10:
            card_num = "F"
        print("|  {}  |".format(card_num), end=" ")
    
    print()        
    print("| / \ | " * len(cards))
    print("|/   \| " * len(cards))
    print("+=====+ " * len(cards))
        
    
def printCards(playerCards, cpuCards):
    print()
    print("The player has the following cards: ")
    printCardsList(playerCards) 
    """ for i in playerCards:
        printCardsList(i) """
    print()
    print("The CPU has the following cards:")
    printCardsList(cpuCards) 
    """ for i in cpuCards:
        printCardsList(i) """
    """ print(i, end = " ") """
    print("\n")

if __name__ == '__main__':
    cards = fillUpCards()
    
    isWin, isBust = False, False
    isGameOver = False
    playerTurn = True
    
    playerCards = list()
    cpuCards = list()
    playerCards, cards = starterDeck(playerCards, cards)
    cpuCards, cards = starterDeck(cpuCards, cards)
    
    gameStart = ""
    print("\nWelcome to Blackjack!")
    
    print("\nIt is worth noting that cards may have a 0.5 sec. delay")
    print("so that the user isn't overwhelmed by the amount of things going on mid-game.\n")
    

    while gameStart != "S" and gameStart != "s":
        gameStart = input("Type in \"S\" or \"s\" to start the game!\n")
    
    
    while not isGameOver:
        
        time.sleep(0.5)
        printCards(playerCards, cpuCards)
        
        if playerTurn:
            isGameOver = checkSums(playerCards, playerTurn, isWin)
            if isGameOver:
                printCards(playerCards, cpuCards)
                break
            
            playerMove = ""
            while playerMove != "H" and playerMove != "h" and playerMove != "S" and playerMove != "s":
                playerMove = input("Hit or stand? [H/S]\n")
                if playerMove == "H" or playerMove == "h":
                    drawn_card, cards = hit(cards)  
                    playerCards.append(drawn_card)
                elif playerMove == "S" or playerMove == "s":
                    pass
                
            isGameOver = checkSums(playerCards, playerTurn, isWin)
            if isGameOver:
                printCards(playerCards, cpuCards)
                break
                
            playerTurn = False
        else:
            isGameOver = checkSums(cpuCards, playerTurn, isWin)
            if isGameOver:
                printCards(playerCards, cpuCards)
                break
            
            cpuMove = choice(["H", "S"])
            print("The CPU is thinking...")
            time.sleep(2.5)
            print("THE CPU CHOSE: " + cpuMove)
            
            if cpuMove == "H":
                print("The CPU chose to HIT!")
                drawn_card, cards = hit(cards)
                cpuCards.append(drawn_card)
            elif cpuMove == "S":
                print("The CPU chose to STAND!")
                pass
            
            isGameOver = checkSums(cpuCards, playerTurn, isWin)
            if isGameOver:
                printCards(playerCards, cpuCards)
                break

            playerTurn = True
    