class Food(object):
  def __init__(self, n, v, w):
    self.name = n
    self.value = v
    self.calories = w
  def getValue(self):
    return self.value
  def getCost(self):
    return self.calories
  def getName(self):
    return self.name
  def density(self):
    return self.getValue()/self.getCost()
  def __str__(self):
    return self.name + ': <' + str(self.value)\
         + ', ' + str(self.calories) + '>'
count = 0
def maxVal(toConsider, avail):
  """Assumes toConsider a list of items, avail a weight
     Returns a tuple of the total value of a solution to the
     0/1 knapsack problem and the items of that solution

     Accepts (list:items, int:availableweight)
     Returns (int:score, list:items)
  """
  global count
  count += 1
  print(' ')
  print(count, "maxVal called:", [c.getName() for c in toConsider], "| Avail:", avail)
  # base case: return nothing if nothing left to consider or no more space
  if toConsider == [] or avail == 0:
    print('Nothing to consider or no weight left')
    result = (0, ())
  # if left branch cant be taken anymore, just look at right
  elif toConsider[0].getCost() > avail:
    print('Next item (' + toConsider[0].getName() + ') is too big. Cross out left.')
    #Explore right branch only
    result = maxVal(toConsider[1:], avail)
  # if left can be taken then look at both
  else:
    # nextItem is [0] because it is left first depth first
    nextItem = toConsider[0]
    print('Took:', nextItem.getName())
    # Explore left branch
    # left is with nextitem inside
    # we call maxVal without nextItem
    # and remove its cost from avail weight
    # and add its value to the output value

    withVal, withToTake = maxVal(toConsider[1:],
                   avail - nextItem.getCost())
    withVal += nextItem.getValue()

    #Explore right branch without taking anything from nextItem
    withoutVal, withoutToTake = maxVal(toConsider[1:], avail)

    print('Now comparing...')
    print(withVal, [w.getName() for w in withToTake + (nextItem,)])
    print(withoutVal, [w.getName() for w in withoutToTake])
    # Choose better branch
    # why are we getting better val here?
    # couldn't right have better value later on?
    if withVal > withoutVal:
      print('Left is better than right')
      # we add in nextItem here only. Why?
      # we are adding back nextItem here because
      # we needed to consider what else could fit in the knapsack
      # without selecting the item again
      # !! we will always take withVal over withoutVal
      result = (withVal, withToTake + (nextItem,))
      print('Recording best so far..', result[0], [r.getName() for r in result[1]])
    else:
      print('Right is better than left')
      # as expected, we just assign value without to result
      # we just go right (without taking)
      result = (withoutVal, withoutToTake)
      print('Recording best so far..', result[0], [r.getName() for r in result[1]])
  print(count, 'Returning:', result[0], [r.getName() for r in result[1]])
  return result

def testMaxVal(foods, maxUnits, printItems = True):
  print('Use search tree to allocate', maxUnits,
      'calories')
  val, taken = maxVal(foods, maxUnits)
  print('Total value of items taken =', val)
  if printItems:
    for item in taken:
      print('   ', item)

names = ['wine', 'beer', 'pizza', 'burger', 'fries',
     'cola', 'apple', 'donut', 'cake'][:2]
values = [89,90,95,100,90,79,50,10][:2]
calories = [123,154,258,354,365,150,95,195][:2]
foods = buildMenu(names, values, calories)

print([str(f) for f in foods])
print('------------------------')
testMaxVal(foods, 350)
