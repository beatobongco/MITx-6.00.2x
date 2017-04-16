import random

def noReplacementSimulation(numTrials):
  '''
  Runs numTrials trials of a Monte Carlo simulation
  of drawing 3 balls out of a bucket containing
  3 red and 3 green balls. Balls are not replaced once
  drawn. Returns the a decimal - the fraction of times 3
  balls of the same color were drawn.
  '''
  num_success = 0
  bucket = ['R'] * 3 + ['G'] * 3

  for _ in range(numTrials):
    hand = random.sample(bucket, 3)

    if hand in (['R'] * 3, ['G'] * 3):
      num_success += 1

  return num_success / numTrials
