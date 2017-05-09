import random
random.seed(0)

def drawing_without_replacement_sim(numTrials):
  '''
  Runs numTrials trials of a Monte Carlo simulation
  of drawing 3 balls out of a bucket containing
  4 red and 4 green balls. Balls are not replaced once
  drawn. Returns a float - the fraction of times 3
  balls of the same color were drawn in the first 3 draws.
  '''
  results = []
  for _ in range(numTrials):
    bucket = list('RRRGGG')
    _result = ''
    for _ in range(3):
      random.shuffle(bucket)
      _result += bucket.pop()
    results.append(_result)

  success = 0
  for r in results:
    if r in ('RRR', 'GGG'):
      success += 1

  return success / len(results)
