############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
import random
from art import logo
#first pick number from the list 
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_card():
  return cards[random.randint(0,len(cards)-1)]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

leaving = False
while leaving == False:
  play_game=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

  print(logo)
  if play_game == 'n':
    print("Good bye")
    leaving = True
  elif play_game == 'y':
    user_value=[]
    computer_value = []
    for repeat in range(2):
      user_value.append(deal_card())
      computer_value.append(deal_card())
    print(f"Your cards: {user_value}, current score: {sum(user_value)}")
    print(f"Computer's first card: {computer_value[0]}")
    #Hint 6: Create a function called calculate_score() that takes a List of cards as input 
    #and returns the score. 
    #Look up the sum() function to help you do this.
    #Detect when computer or user has a blackjack. (Ace + 10 value card).
    def calculate_score(arr):
      #Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
      if 11 in arr and 10 in arr and len(arr)==2:
        return 0
      #Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
      elif 11 in arr and sum(arr)>21:
        arr[arr.index(11)]=1
      return sum(arr)
    
    exit = False
    
    #Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
    #Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
    
    #Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
    
    while exit is False:
      if calculate_score(computer_value)==0:
        exit = True
      elif calculate_score(user_value)==0:
        exit = True
      elif  calculate_score(user_value)>21:
        exit = True
      else:
        draw_another = input("Type 'y' to get another card, type 'n' to pass: ")
        if draw_another =='y':
          user_value.append(deal_card())
          print(f"Your cards: {user_value}, current score: {sum(user_value)}")
        elif draw_another == 'n':
          exit = True
    
      
    
    #Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
    while sum(computer_value)<17:
      computer_value.append(deal_card())
    #Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
    def compare(computer_value,user_value):
      if calculate_score(computer_value)==0:
        print("user lost")
      elif calculate_score(user_value)==0:
        print("user won")
      elif calculate_score(computer_value)==calculate_score(user_value):
        print("draw")
      elif calculate_score(user_value) > calculate_score(computer_value) and calculate_score(user_value) <=21 or calculate_score(computer_value) >21:
        print("user won")
      else:
        print("user lost")
    #Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
    
    
    
    # Compare user and computer scores and see if it's a win, loss, or draw.
    
    # Print out the player's and computer's final hand and their scores at the end of the game.
    
    print(f" Your final hand: {user_value}, final score: {sum(user_value)}")
    print(f"Computer's final hand: {computer_value}, final score {sum(computer_value)}")
    compare(computer_value,user_value)
else:
  print("wrong input")