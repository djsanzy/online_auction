bidders = {}

def calc_bid(bids):
    highest_bid = 0
    winner = ""
    for key in bids:
        bid_amount = bids[key]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = key
    print(f"The winner is {winner} with the bid of {highest_bid}")


bid_finished = False

while not bid_finished:
    name = input("What is your name? \n")
    bid = int(input("What is your bid? \n$"))
    bidders[name] = bid
    still_bidders = input("Are there are more bidders. Type 'yes' or 'no'. \n").lower()
    if still_bidders == 'no':
        bid_finished = True
        calc_bid(bidders)
    elif still_bidders != 'yes' and still_bidders != 'no':
        bid_finished = True
        print("Wrong input. Type 'yes' or 'no'.")

