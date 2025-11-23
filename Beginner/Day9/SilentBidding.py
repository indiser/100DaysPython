import os
import auction_art

auction_art.logo()

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

bidderInfo={}
while True:
    bidderName=input("Enter your name:\n")
    bidderAmount=int(input("Enter you bid amount:\n$"))
    bidderInfo[bidderName]=bidderAmount
    moreBidders=input("Are there any other bidders? Type 'yes' or 'no'\n").lower()
    if moreBidders=="yes":
        clear()
        continue
    else:
        maxBid=float('-inf')
        maxBidder=None
        for key,value in bidderInfo.items():
            if value > maxBid:
                maxBid=value
                maxBidder=key
        print(f"{maxBidder} has the highest bid of ${maxBid}")
        break
