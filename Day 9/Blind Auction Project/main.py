# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

import art

print(art.logo)

bids = {}
other_bidders = "yes"

while other_bidders == "yes":
    name = input("What is your name? ")
    bid = int(input("What's your bid? $"))
    bids[name] = bid
    other_bidders = input("Are there other bidders? Type 'yes' or 'no'. \n").lower()
    print("\n" * 100)

# sa ovim se cisti ekran tj. radi se print 100 novih redova
print("\n" * 100)

best_bid_name = ""
best_bid_amount = 0

for name, bid in bids.items():
    if bid > best_bid_amount:
        best_bid_amount = bid
        best_bid_name = name

print(f"The winner is {best_bid_name} with a bid of ${best_bid_amount}. 👏👏👏")



