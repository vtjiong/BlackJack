import art
import random
from replit import clear
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Function to deal card initially
def initial_deal(cards2):
  for i in range(2):
    cards2=deal_cards(cards2)
  return cards2

# Function to deal card
def deal_cards(cards3):
  card = random.choice(cards)
  if card==11:
    if sum(cards3)+card>21:
      card=1
  cards3.append(card)
  return cards3

#Function to deal card and find the winner
def compare(user_cards,computer_cards):
  print(f"Yours final hand: {user_card}, final score:{sum(user_card)}")
  print(f"Computer's final hand: {computer_card}, final score: {sum(computer_card)}")
  if sum(user_cards)>21 and sum(computer_cards)<21 or(sum(user_cards)<sum(computer_cards)):
    print("You lose")
  elif (sum(computer_cards)>21 and sum(user_cards)<21) or(sum(user_cards)>sum(computer_cards)):
    print("You win")
  elif sum(user_cards)==sum(computer_cards):
    print("It's a draw!")

#Computer's algorithm in playing the game
def computer_sequence(user_cards,computer_cards):
  if sum(user_cards)>21:
    return (computer_cards)
  else:
    while sum(computer_cards)<sum(user_cards):
      computer_cards=deal_cards(computer_cards)
    return (computer_cards)

#Main function that runs the game
complete=False
print (art.logo)
decision= input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if decision=="y":
  while complete==False:
    user_card=initial_deal([])
    computer_card=initial_deal([])
    print(f"Your cards: {user_card}, current score: {sum(user_card)}")
    print(f"computers first card: {computer_card[0]}")
    deal_again=True
    while deal_again==True:
      decision2=input("Type 'y' to get another card, type 'n' to pass: ")
      if decision2=="y":
        user_card = deal_cards(user_card)
        if sum(user_card)>21:
          break
        else:
          print(f"Your cards: {user_card}, current score: {sum(user_card)}")
          print(f"computers first card: {computer_card[0]}")
      else:
        deal_again=False
    computer_card=computer_sequence(user_card,computer_card)
    compare(user_card,computer_card)
    decision3=input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
    if decision3=="y":
      clear()
      print(art.logo)
    else:
      complete=True