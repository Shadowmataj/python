from art import logo
import random

print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_list = []
dealer_list = []
pass_turn = False


def draw_a_card():
    return random.choice(cards)

def show_dealer_list(list_to_hide):
    print_list = "["
    for num in range(0,len(list_to_hide)):
        if num == 0:
            print_list += f"{list_to_hide[num]}"
        else:
            print_list += f", X"
    print_list += "]"
    return print_list

def check_aces(list_to_check):
    if 11 in list_to_check and sum(list_to_check) > 21:
        list_to_check.remove(11)
        list_to_check.append(1)
    return list_to_check

def pass_function():
    pass_turn_selection = input("Type 'y' to get another card, type 'n' to pass: ")

    if pass_turn_selection.lower() == "n":
        return True

def turn(p_list,d_list):

    if sum(p_list) > 21:
        print("You are busted!")
    else:
        print(f"Your cards: {p_list}, current score: {sum(p_list)}")
    if sum(d_list) > 21:
        print("Computer is busted!")
    else:
        print(f"Computer cards: {show_dealer_list(d_list)}, first card: {d_list[0]}")


for times in range(0,2):
    player_list.append(draw_a_card())
    dealer_list.append(draw_a_card())

print(f"Your cards: {player_list}, current score: {sum(player_list)}")
print(f"Computer cards: {show_dealer_list(dealer_list)}, first card: {dealer_list[0]}")

pass_turn = pass_function()

while not pass_turn:
    player_list.append(draw_a_card())
    player_list = check_aces(player_list)
    if sum(dealer_list) < 17:
        dealer_list.append(draw_a_card())
        dealer_list = check_aces(dealer_list)
    turn(p_list=player_list, d_list=dealer_list)

    if sum(player_list) > 21:
        pass_turn = not pass_turn
    else:
        pass_turn = pass_function()

while sum(dealer_list) < 17:
    dealer_list.append(draw_a_card())
    dealer_list = check_aces(dealer_list)

print(f"Your cards: {player_list}, total score: {sum(player_list)}")
print(f"Computer cards: {dealer_list}, total card: {sum(dealer_list)}")

players_totals = {
    "player": sum(player_list),
    "dealer": sum(dealer_list)
}
winners = {}
for player in players_totals:
    if players_totals[player] <= 21:
        winners[player] = players_totals[player]

if len(winners) == 0:
    print("Both lose!")
elif len(winners) == 1:
    print(f"The winner is {list(winners.keys())[0]} with {winners[list(winners.keys())[0]]}")
elif len(winners) == 2 and players_totals["player"] == players_totals["dealer"]:
    print("It's a draw!")
elif len(winners) == 2:
    print(f"The winner is {max(winners, key=winners.get)} with {winners[max(winners, key=winners.get)]}")

