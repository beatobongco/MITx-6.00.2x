def stdDevOfLengths(L):
  """
  L: a list of strings

  returns: float, the standard deviation of the lengths of the strings,
    or NaN if L is empty.
  """
  if not L:
    return float('NaN')

  lengths = [len(e) for e in L]
  mean = sum(lengths) / len(lengths)
  vals = [(e - mean) ** 2 for e in lengths]

  return (sum(vals) / len(vals))**.5
