from fractions import Fraction

# Justifying the answers to numbers 8 and 9
# Assume we roll 2 four sided dice.

# 8. What is P({first roll larger than second roll})?

N = 4 #number of sides per die

# Let's model the number of rolls
probability = 0
for x in range(1, N + 1):
  # First roll is x, what is probability of rolling lower?
  # ((x - 1) / N) - probability we will roll anything less than x
  probability += ((x - 1) / N) * (1 / N) # multiply by 1/N because there's only 1/N chance of this case
print(Fraction(probability))

# 9. What is P({at least one roll is equal to 4})?

# We can do this easily by doing 1 - X where X is the proability of 4 never showing up
print(Fraction(1- (3/4) * (3/4)))
