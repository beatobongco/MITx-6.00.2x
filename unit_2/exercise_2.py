import random
def genEven():
  '''
  Returns a random even number x, where 0 <= x < 100
  '''
  r = random.randint(0, 99)
  if r % 2 == 0:
    return r
  else:
    return genEven()

# tests random 1000x so make sure there's no odd numbers

for x in range(0, 1000):
  assert genEven() % 2 == 0
