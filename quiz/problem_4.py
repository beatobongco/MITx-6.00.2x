def greedySum(L, s):
  """
    input: s, positive integer, what the sum should add up to
           L, list of unique positive integers sorted in descending order

    Use the greedy approach where you find the largest multiplier for
    the largest value in L then for the second largest, and so on to
    solve the equation s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)

    return: the sum of the multipliers or "no solution" if greedy approach does
            not yield a set of multipliers such that the equation sums to 's'
  """

  def get_sum(L, mults):
    return sum([x * y for x, y in zip(L, mults)])

  mults = []

  for n in L:
    candidate = 1
    while True:
      if get_sum(L, mults) + n * candidate > s:
        candidate -= 1
        mults.append(candidate)
        break
      candidate += 1

    if get_sum(L, mults) == s:
      return sum(mults)

  return 'no solution'

assert greedySum([3, 2, 1], 3) == 1
assert greedySum([3, 2, 1], 10) == 4
assert greedySum([3, 3, 3], 10) == 'no solution'
