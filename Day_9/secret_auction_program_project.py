"""
    This program implements an algorithm for secret auctioning
"""
from art_work import logo

from replit import clear


print("Welcome to Today's Auction\n")

# Insert Art work here
print(logo)


print("\n")


# Initiating the Loop with the condition

another_bid  = "yes"

# Create an empty dictionary to store all bids
bids = {}

while another_bid == "yes":

    # Ask for the name of the bidder
    bidder_name = input("\nPlease enter your name.\n")

    # Ask of the bid price
    bid_price = int(input("\nPlease enter your bid Price (without currency symbol).\n"))

    # Add the bidder_name and bid_price to the empty_dict
    bids[bidder_name] = bid_price

    # Ask if there are other users who want to bid?
    another_bid = input("\nAre there other users who want to bid? Yes or No\n").lower()

    # Lets clear screen if there is another bid
    if another_bid == "yes":
        clear()



# Printing out the winner
max_value = max(bids.values())

max_bidder_list = [key for key, value in bids.items() if value == max_value] 

max_bidder = "".join(max_bidder_list)

print(f"Thanks for all the bids. The winner of this bid-round is {max_bidder}")
