import random
def deterministicNumber():
  '''
  Deterministically generates and returns an even number between 9 and 21
  '''
  return 10

def stochasticNumber():
  '''
  Stochastically generates and returns a uniformly distributed even number between 9 and 21
  '''
  r = random.randint(9, 21)
  if r % 2 == 0:
    return r
  else:
    return stochasticNumber()
