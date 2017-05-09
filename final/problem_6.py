import numpy as np
from itertools import combinations

def find_combination(choices, total):
  """
  choices: a non-empty list of ints
  total: a positive int

  Returns result, a numpy.array of length len(choices)
  such that
    * each element of result is 0 or 1
    * sum(result*choices) == total
    * sum(result) is as small as possible
  In case of ties, returns any result that works.
  If there is no result that gives the exact total,
  pick the one that gives sum(result*choices) closest
  to total without going over.
  """
  all_combos = []

  for i in range(1, len(choices) + 1):
    all_combos += [x for x in combinations(choices, i) if sum(x) <= total]

  all_combos.sort(key=lambda k: (-sum(k), len(k)))

  if not all_combos:
    return np.zeros(len(choices), dtype=np.int)

  result = []
  for c in choices:
    if c in all_combos[0]:
      result.append(1)
    else:
      result.append(0)

  return np.array(result)


assert list(find_combination([1, 2, 2, 3], 4)) in ([0, 1, 1, 0], [1, 0, 0, 1])
assert list(find_combination([1, 1, 3, 5, 3], 5)) == [0, 0, 0, 1, 0]
assert list(find_combination([1, 1, 1, 9], 4)) == [1, 1, 1, 0]
assert list(find_combination([1, 3, 4, 2, 5], 16)) == [1, 1, 1, 1, 1]
