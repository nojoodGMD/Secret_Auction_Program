import os
from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)
print("Welcome to the Secret Auction Program")

finish_bidding = False
participants = {}

while not finish_bidding:
  name = input("Enter your name: ")
  price = float(input("Enter the Bid value: $"))

  participants[name] = price

  repreat = input("Are there more people? 'Y' or 'N': ").lower()
  if repreat == "n":
    finish_bidding = True
  os.system('cls' if os.name == 'nt' else 'clear')

#find the highest value
highest_bid = -1
highest_bidder = ""

for person in participants:
  if participants[person] > highest_bid:
    highest_bid = participants[person]
    highest_bidder = person

print(f"The highest bidder was {highest_bidder} with {highest_bid}$")