from replit import clear

bid_live = True
bid_dict = {}
while bid_live: 
    name = input("What is your name? ")
    bid = int(input("What is your bid? $ "))


    bid_dict[name] = bid

    bid_still_live = input("Are there any more bidders? 'yes' or 'no' ")
    if bid_still_live == "yes":
        clear()
    else:
        winner = ""
        highest_bid = 0
        for value in bid_dict:
            bid_amount = bid_dict[value]
            if bid_amount > highest_bid:
                highest_bid = bid_amount
                winner = value
        print(f"The winner is {winner} with a bid of {highest_bid}")


