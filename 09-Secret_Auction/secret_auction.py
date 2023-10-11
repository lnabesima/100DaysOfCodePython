import os

from secret_auction_art import logo

bidders = []
highest_bid = 0
highest_bidder_name = ""


def add_new_bidder(new_name, new_bid):
    new_bidder = {"name": new_name, "bid": new_bid}
    bidders.append(new_bidder)


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


clear_console()
print(logo)

while True:
    print("Welcome to the secret audition program.")
    name = input("What's your name?: ")
    bid = int(input("What's your bid?: "))
    add_new_bidder(name, bid)
    another_bidder = input("Are there any other bidders? [Y]es or [N]o: ")
    if another_bidder.lower() == 'y':
        clear_console()
        continue
    elif another_bidder.lower() == 'n':
        break
    else:
        print("Please only type Y (for yes) or N (for no)")

for bidder in bidders:
    if bidder['bid'] > highest_bid:
        highest_bid = bidder['bid']
        highest_bidder_name = bidder['name']

print(f"The highest bid id ${highest_bid}, from {highest_bidder_name}. Congratulations, {highest_bidder_name}!")
