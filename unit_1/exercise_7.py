class WeightedEdge(Edge):
  def __init__(self, src, dest, weight):
    # Your code here
    Edge.__init__(self, src, dest)
    self.weight = weight
  def getWeight(self):
    # Your code here
    return self.weight
  def __str__(self):
    # Your code here
    return Edge.__str__(self) + '(' + self.getWeight() + ')'
