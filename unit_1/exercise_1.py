# generate all combinations of N items
def powerSet(items):
  N = len(items)
  # enumerate the 2**N possible combinations
  for i in range(2**N):
    combo = []
    for j in range(N):
      # test bit jth of integer i
      print('i', i, 'j', j, i>>j)
      if (i >> j) % 2 == 1:
        combo.append(items[j])
    yield combo


for x in powerSet([0,1,2]):
  print(x)

def yieldAllCombos(items):
  N = len(items)
  # enumerate the 3**N possible combinations
  for i in range(3**N):
    bag = ([], [])
    for j in range(N):
      # test bit jth of integer i
      if (i >> j) % 3 == 1:
        bag[0].append(items[j])
      elif (i >> j) % 3 == 2:
        bag[1].append(items[j])
    yield bag

for x in yieldAllCombos([0,1,2]):
  print(x)
