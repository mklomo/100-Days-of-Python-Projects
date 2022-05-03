"""
    This program implements an algorithm for playing the BlackJack
"""


import random

from replit import clear

from art_work import logo


# Do we have a blackjack?
def is_blackjack(player_card_list, computer_card_list):
    # Define a blackjack
    black_jack = [11, 10]

    # Check if the user or computer has a blackjack
    if sum(computer_card_list) == sum(black_jack) and len(computer_card_list) == 2:
        return "\nComputer has blackjack\n"

    elif sum(player_card_list) == sum(black_jack) and len(player_card_list) == 2:
        return "\Player has blackjack\n"

    # Check if players score is above 21
    if sum(player_card_list) > 21:
        if 11 in player_card_list:
            # Replace the 11 with 1
            new_player_card_list = player_card_list[:]
            for index, card in enumerate(new_player_card_list):
                if card == 11:
                    player_card_list[index] = 1

            # Now check whether this new list is still over 21
            if sum(player_card_list) > 21:
                return "\nYou Lose\n"

            else:
                new_card = input(
                    "Would you like a new card? Type 'y' for YES and 'n' for NO: "
                ).lower()
                if new_card == "n":
                    # Computer plays
                    if sum(computer_card_list) < 17:
                        computer_card_list.append(random.choice(cards))

                    print(
                        f"    The Computer has {computer_card_list}, current total: {sum(computer_card_list)}\n"
                    )

                    if sum(computer_card_list) >= 21:
                        return "\nComputer wins\n"

                    elif sum(computer_card_list) == sum(player_card_list):
                        return "\nSame Score\n"

                    elif sum(player_card_list) > sum(computer_card_list):
                        return "\nPlayer wins\n"

                    elif sum(player_card_list) < sum(computer_card_list):
                        return "\nYou Lose\n"

                if new_card == "y":
                    player_card_list.append(random.choice(cards))
                    print(
                        f"\nYour Cards are: {player_card_list}, and current score: {sum(player_card_list)}\n"
                    )
                    return is_blackjack(
                        player_card_list=player_card_list,
                        computer_card_list=computer_card_list,
                    )

        else:
            return "\nYou Lose\n"


    else:
        new_card = input(
            "Would you like a new card? Type 'y' for YES and 'n' for NO: "
        ).lower()
        if new_card == "n":
            # Computer plays
            while sum(computer_card_list) < 17:
                computer_card_list.append(random.choice(cards))

            print(
                f"\nThe Computer has {computer_card_list}, current total: {sum(computer_card_list)}\n"
            )

            if sum(computer_card_list) >= 21:
                return "\nComputer wins\n"

            elif sum(computer_card_list) == sum(player_card_list):
                return "\nSame Score\n"

            elif sum(player_card_list) > sum(computer_card_list):
                return "\nPlayer wins\n"

            elif sum(player_card_list) < sum(computer_card_list):
                return "\nYou Lose\n"

        if new_card == "y":
            player_card_list.append(random.choice(cards))
            print(
                f"\nYour Cards are: {player_card_list}, and current score: {sum(player_card_list)}\n"
            )
            return is_blackjack(
                player_card_list=player_card_list, computer_card_list=computer_card_list
            )


if __name__ == "__main__":
    # Ask prompt
    print("\n")
    play_game = input(
        "Would you like to play the game of Blackjack? Type 'y' for Yes and 'n' for No: "
    ).lower()

    if play_game == "y":
        print("\n")

        print("Welcome to Marvin's Blackjack")

        print("\n")

        print(logo)

        print("\n")

        # List of cards to be dealt

        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

        # Dealing cards to users
        player_card_list = []

        computer_card_list = []

        # Dealing first 2 random cards
        for each_round in range(2):
            player_card_list.append(random.choice(cards))
            computer_card_list.append(random.choice(cards))

        print(
            f"      Your Cards are: {player_card_list}, current score is: {sum(player_card_list)}\n"
        )

        print(f"      The computer's card is: {computer_card_list}\n")

        output = is_blackjack(
            player_card_list=player_card_list, computer_card_list=computer_card_list
        )
        print(output)


    else:
        print("\nThank you and Goodbye!\n")
