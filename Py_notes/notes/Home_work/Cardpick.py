import random

suits =['Heart','Spade','Diamond','Club']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A' ]

random_suit = random.choice(suits)
random_rank = random.choice(ranks)
print(f"The card you chose is a {random_suit} {random_rank}")
