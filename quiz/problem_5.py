def max_contig_sum(c):
  king = 0
  # clone so we dont modify original by popping
  cloned_c = c.copy()
  while len(cloned_c) > 0:
    current = 0
    for n in cloned_c:
      current += n
      if current > king:
        king = current
    else:
      cloned_c.pop(0)
  return king


assert max_contig_sum([3, 4, -1, 5, -4]) == 11
assert max_contig_sum([3, 4, -8, 15, -1, 2]) == 16
assert max_contig_sum([1, -99, -10, -15]) == 1
assert max_contig_sum([-99, -10, -15, 1]) == 1


def max_contig_sum2(c):
  current = 0
  king = 0
  for n in c:
    if current + n > 0:
      current += n
      if current > king:
        king = current
    else:
      current = 0
  else:
    return king


assert max_contig_sum2([3, 4, -1, 5, -4]) == 11
assert max_contig_sum2([3, 4, -8, 15, -1, 2]) == 16
assert max_contig_sum2([1, -99, -10, -15]) == 1
assert max_contig_sum2([-99, -10, -15, 1]) == 1
assert max_contig_sum2([1, -99, -10, 100]) == 100
assert max_contig_sum2([-1, -1, 100, -1, -1]) == 100
