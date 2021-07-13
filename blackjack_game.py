from blackjack_art import logo
from random import choice

def draw(card_list):
    return choice(card_list)
    
def score(hand):
    score = 0
    for cards in hand:
        score += cards
    return score

def result():
        if score(player_hand) > 21:
            return 'You went over. You lose.'
        elif score(player_hand) > score(dealer_hand):
            return 'You win.'
        elif score(player_hand) > score(dealer_hand):
            return 'You lose.'
        elif score(player_hand) == score(dealer_hand):
            return 'How boring. Tied.'


cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_hand = [draw(cards), draw(cards)]
dealer_hand = [draw(cards), draw(cards)]

print(logo, '\nWelcome to PyBlackjack.')

while True:
    print(f'\nYour cards {player_hand}, your score: {score(player_hand)}')
    print(f'Computer\'s first card: {dealer_hand[0]}')
    new_draw = input('Enter 1 to get another card and 0 to pass: ')

    if new_draw == '1':
        player_hand.append(draw(cards))

        if score(player_hand) >= 21:
            print(f'\nYour final hand was {player_hand}.')
            print(f'And you score {score(player_hand)} points.')
            print(f'Computer\'s final hand was: {dealer_hand}.')
            print(f'And it scores {score(dealer_hand)} points.')
            print(result())
            break

    elif new_draw == '0':
        print(f'\nYour final hand was {player_hand}.')
        print(f'And you score {score(player_hand)} points.')
        print(f'Computer\'s final hand was: {dealer_hand}.')
        print(f'And it scores {score(dealer_hand)} points.')
        print(result())
        break
