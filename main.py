"""
LEVEL : B E G I N N E R.
-----------------------------------------------------------
Project - The Secret Auction.
-----------------------------------------------------------
"""

import art

print(art.logo)
bidders = {}
check = True


def highest_bidder(bidders):
    highest_bid = 0
    for name in bidders:
        if bidders[name] > highest_bid:
            highest_bid = bidders[name]
            winner = name
    print("Bid is over!!!")
    print(f"Highest bidder is {winner}, who bet ${highest_bid}.")
    print(art.logo2)


while check == True:
    name = input("What is your name? : ")
    bid = int(input("What is your bid? : "))
    bidders[name] = bid
    condition = input("Are there any other bidders 'yes' or 'no'? : ").lower()
    if condition == "no":
        check = False

highest_bidder(bidders)
