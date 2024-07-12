import random
from replit import clear

# input assign the computer and the player two cards from a list, 
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
clear()
if input("Would yo like to play blackjack? 'y' or 'n' ").lower() == "y":
    blackjack_on = True
else:
    blackjack_on = False

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_cards():
    random.shuffle(cards)
    player_cards = []
    computer_cards = [] 
    for _ in range(2):
        player_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))
    return computer_cards, player_cards

def sum_of_cards(cards):
    total_sum = sum(cards)
    return total_sum

def compare(player_sum, computer_sum):
    if player_sum == computer_sum:
        return "It's a draw!"
    elif computer_sum == 0:
        return "Computer has Blackjack! You lose."
    elif player_sum == 0:
        return "You have Blackjack! You win."
    elif player_sum > 21:
        return "You went over. You lose."
    elif computer_sum > 21:
        return "Computer went over. You win."
    elif player_sum > computer_sum:
        return "You win!"
    else:
        return "You lose."


while blackjack_on:
    computer_cards, player_cards = deal_cards()
    player_sum = sum_of_cards(player_cards)
    computer_sum = sum_of_cards(computer_cards)
    
    print(f"Your cards: [{player_cards[0]}, {player_cards[1]}], current sum: {player_sum}")
    print(f"Dealer cards: [{computer_cards[0]}, X]")
    hit_stand = input("Type 'y' to HIT or 'n' to stand \n: ")
    if hit_stand == "y":
        player_cards.append(random.choice(cards))
        player_sum = sum_of_cards(player_cards)
        print(f"You hit! Recived a {player_cards[2]}, cards: [{player_cards[0]}, {player_cards[1]}, {player_cards[2]}], current sum: {player_sum}")

    else:
        blackjack_on = False   

while computer_sum < 17:          
    print(f"You stand on: {player_sum}")
    print(f"Dealer cards: [{computer_cards[0]}, {computer_cards[1]}] He draws a card!")
    computer_cards.append(random.choice(cards))
    computer_sum = sum_of_cards(computer_cards) 
    print(f"dealer sum: {computer_sum}")

print(f"Your final hand: {player_sum},")
print(f"Computer's final hand: {computer_sum}")
print(compare(player_sum, computer_sum))
