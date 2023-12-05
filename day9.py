bids = {}
def find_highest_bidder(bidding_record):
    highest = 0
    winner =  ""
    for bidder in bidding_record:
        cash = bidding_record[bidder]
        if cash > highest:
            highest = cash
            winner = bidder
    print(f"the winner is {winner} with the bid of ${highest}")

condition = True

while  condition:
    name = input("whats your name : ")
    price = int(input("whats your bid :$"))
    bids[name]=price
    ask = input("is there another bider type yes or no:").lower()
    
    if ask == "no":
        condition == True
        find_highest_bidder(bids)