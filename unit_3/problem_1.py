import random

random.seed(0)


class SimpleVirus(object):

  def __init__(self, maxBirthProb, clearProb):
    self.clearProb = clearProb
    self.maxBirthProb = maxBirthProb

  def getMaxBirthProb(self):
    return self.maxBirthProb

  def getClearProb(self):
    return self.clearProb

  def doesClear(self):
    return random.random() <= self.getClearProb()

  def reproduce(self, popDensity):
    if random.random() < self.getMaxBirthProb() * (1 - popDensity):
      return SimpleVirus(self.getMaxBirthProb(), self.getClearProb())
    else:
      raise NoChildException


class Patient(object):

  def __init__(self, viruses, maxVirusPop):
    self.viruses = viruses
    self.maxVirusPop = maxVirusPop

  def getViruses(self):
    return self.viruses

  def addVirus(self, newVirus):
    return self.viruses.append(newVirus)

  def removeVirus(self, virus):
    self.viruses.remove(virus)

  def getPopDensity(self):
    return self.getTotalPop() / self.maxVirusPop

  def getTotalPop(self):
    return len(self.getViruses())

  def update(self):
    for virus in self.getViruses():
      if virus.doesClear():
        self.removeVirus(virus)

    for virus in self.getViruses():
      try:
        self.addVirus(virus.reproduce(self.getPopDensity()))
      except NoChildException:
        pass

    return len(self.getViruses())
